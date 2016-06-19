"""
conway.game
~~~~~~~~~~~~~~~
This module contains an implementation of Conway's Game of Life

Inspired by Jack Diederich's talk `Stop Writing Classes`
http://pyvideo.org/video/880/stop-writing-classes

Partially derived from Jason Keene's gist:
https://gist.github.com/jasonkeene/2140276
"""
from itertools import chain, product

# product((-1, 0, 1), (-1, 0, 1)) # remove (0,0)
NEIGHBOR_SET = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1))

def neighbors(point):
    """
    Returns the set of adjacent points to the given point.
    """
    x, y = point
    return set((x + dx, y + dy) for dx, dy in NEIGHBOR_SET)

class Board(object):
    """The :class:`Board <Board>` object, which contains
    the cells of a given Conway pattern.
    """

    def __init__(self, pattern, size=100):
        """Takes string representations of GoL patterns from
        http://www.argentum.freeserve.co.uk/lex.htm and returns"""
        self.size = size -1
        self.points = set()
        self.pattern = pattern
        self.frame_num = 0
        self.frames = []

        i, j = 0, 0
        for char in pattern:
            if char == '\n':
                i = 0
                j += 1
            elif char == '1':
                i += 1
            elif char == '0':
                self.points.add((i, j))
                i += 1

    def __hash__(self):
        return hash(frozenset(self.points))

    def __eq__(self, other):
        return other and hash(self) == hash(other)

    def advance(self):
        """
        Moves the board one time step according to the basic rules of Conway's Game of Life:

        From https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life:
        Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by over-population.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        newstate = set()
        recalc = self.points | set(chain(*(neighbors(point) for point in self.points)))
        for point in recalc:
            count = len(self.points & neighbors(point))
            if count == 3 or (count == 2 and point in self.points):
                newstate.add(point)
        self.points = newstate
        return self

    def center(self):
        """
        Computes the centroid of the Board pattern, and shifts the points accordingly.
        """
        center_x, center_y = (sum(dim)/len(self.points) - self.size/2 for dim in zip(*self.points))
        self.points = {(x-center_x, y-center_y) for x, y in self.points}
        return self

    def constrain(self):
        """
        Removes any points outside of the cell's bounding box.
        """
        self.points = set(cell for cell in self.points if self.contains(cell))
        return self

    def contains(self, cell):
        """
        Returns true if a cell is part of the bounding box.
        """
        return all(0 <= v <= self.size for v in cell)

    def scale(self, square_size):
        """
        Turns the board into a series of 0s and 1s scaled up by `square_size`
        """
        line = []
        for i, j in product(range(self.size + 1), range(self.size + 1)):
            line.extend([0]*square_size if (i, j) in self.points else [1]*square_size)
            if j == self.size:
                for _ in range(square_size):
                    yield line
                line = []
