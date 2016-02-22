"""
Sample patterns for Conway's Game of Life, mostly
taken from Stephen Silver's Life Lexicon:
http://www.argentum.freeserve.co.uk/lex.htm
"""

GLIDER = """OOO
            O..
            .O.
         """

BEE = """.........O............
          .......O.O............
          ......O.O.............
          OO...O..O.............
          OO....O.O.............
          .......O.O........OO..
          .........O........O.O.
          ....................O.
          ....................OO"""

FOO = """OO..O
         O...O
         O..OO"""

RATS = """  .....OO.....
            ......O.....
            ....O.......
            OO.O.OOOO...
            OO.O.....O.O
            ...O..OOO.OO
            ...O....O...
            ....OOO.O...
            .......O....
            ......O.....
            ......OO...."""

GROWER = """........OO.......
            .......OO........
            .........O.......
            ...........OO....
            ..........O......
            .................
            .........O..OO...
            .OO.....OO....O..
            OO.....O.....O...
            ..O....O.O...OO..
            ....O..O....OO.O.
            ....OO.......OO..
            ........O....O.OO
            .......O.O..O.OO.
            ........O........"""

GUN = """........................O...........
         ......................O.O...........
         ............OO......OO............OO
         ...........O...O....OO............OO
         OO........O.....O...OO..............
         OO........O...O.OO....O.O...........
         ..........O.....O.......O...........
         ...........O...O....................
         ............OO......................"""

BUCK = """
       ..O.....................
       O.O.....................
       .OO.....................
       ...........O............
       .........O.O............
       ........O.O.............
       .......O..O...........OO
       ........O.O...........OO
       ...OO....O.O............
       ..O.O......O............
       ..O.....................
       .OO.....................
        """


GARDEN = """..O.OOO.....
            OO.O.OOOOO.O
            O.O.OO.O.O..
            .OOOO.O.OOO.
            O.O.OO.OOO.O
            .OOO.OO.O.O.
            ..O...OOO..O
            .O.OO.O.O.O.
            OOO.OOOO.O.O
            OO.OOOO...O.
            .O.O.OO..O..
            .OO.O..OO.O."""

PUFFER = """.OOO...........OOO
            O..O..........O..O
            ...O....OOO......O
            ...O....O..O.....O
            ..O....O........O.
         """

PULSAR = """..OOO...OOO..
            .............
            O....O.O....O
            O....O.O....O
            O....O.O....O
            ..OOO...OOO..
            .............
            ..OOO...OOO..
            O....O.O....O
            O....O.O....O
            O....O.O....O
            .............
            ..OOO...OOO..
         """

REVOL = """ O............O
            OOO....O...OOO
            ...O.O.O..O...
            ..O......O.O..
            ..O.O......O..
            ...O..O.O.O...
            OOO...O....OOO
            O............O"""

GENERATOR =  """................O..
                .OO...........O...O
                OO.OOO.......O.....
                .OOOOO.......O....O
                ..OOOOO.....O.OOOO.
                ......OOO.O.OO.....
                ......OOO....O.....
                ......OOO.OOO......
                ..........OO.......
                ..........OO.......
                ......OOO.OOO......
                ......OOO....O.....
                ......OOO.O.OO.....
                ..OOOOO.....O.OOOO.
                .OOOOO.......O....O
                OO.OOO.......O.....
                .OO...........O...O
                ................O..
             """

PYRO =   """.......O........
            .....OOOOO......
            ....O.....O.....
            .O..O.O.OO.O....
            O.O.O.O....O..O.
            .O..O....O.O.O.O
            ....O.OO.O.O..O.
            .....O.....O....
            ......OOOOO.....
            ........O.......
         """

RING = """  ................O.................
            ..............O.O.O...............
            ............O.O.O.O.O.............
            ..........O.O.O.O.O.O.O...........
            ........O.O.O..OO.O.O.O.O.........
            ......O.O.O.O......O..O.O.O.......
            ....O.O.O..O..........O.O.O.O.....
            .....OO.O..............O..O.O.O...
            ...O...O..................O.OO....
            ....OOO....................O...O..
            ..O.........................OOO...
            ...OO...........................O.
            .O...O........................OO..
            ..OOOO.......................O...O
            O.............................OOO.
            .OOO.............................O
            O...O.......................OOOO..
            ..OO........................O...O.
            .O...........................OO...
            ...OOO.........................O..
            ..O...O....................OOO....
            ....OO.O..................O...O...
            ...O.O.O..O..............O.OO.....
            .....O.O.O.O..........O..O.O.O....
            .......O.O.O..O......O.O.O.O......
            .........O.O.O.O.OO..O.O.O........
            ...........O.O.O.O.O.O.O..........
            .............O.O.O.O.O............
            ...............O.O.O..............
            .................O................"""

BRAIN = """
        .OOO.........OOO.
        O.O.OO.....OO.O.O
        O.O.O.......O.O.O
        .O.OO.OO.OO.OO.O.
        .....O.O.O.O.....
        ...O.O.O.O.O.O...
        ..OO.O.O.O.O.OO..
        ..OOO..O.O..OOO..
        ..OO..O...O..OO..
        .O....OO.OO....O.
        .O.............O.
        """
SPACE_RAKE = """...........OO.....OOOO
                .........OO.OO...O...O
                .........OOOO........O
                ..........OO.....O..O.
                ......................
                ........O.............
                .......OO........OO...
                ......O.........O..O..
                .......OOOOO....O..O..
                ........OOOO...OO.OO..
                ...........O....OO....
                ......................
                ......................
                ......................
                ..................OOOO
                O..O.............O...O
                ....O................O
                O...O............O..O.
                .OOOO................."""

SOME = """  ...........OO...........
    ......OO.O....O.OO......
    ......O..........O......
    .......OO......OO.......
    ....OOO..OOOOOO..OOO....
    ....O..O........O..O....
    .OO.O.O..........O.O.OO.
    .O.O.O............O.O.O.
    ...O................O...
    .O..O..............O..O.
    ....O.......OOO....O....
    O...O.......O.O....O...O
    O...O.......O.O....O...O
    ....O..............O....
    .O..O..............O..O.
    ...O................O...
    .O.O.O............O.O.O.
    .OO.O.O..........O.O.OO.
    ....O..O........O..O....
    ....OOO..OOOOOO..OOO....
    .......OO......OO.......
    ......O..........O......
    ......OO.O....O.OO......
    ...........OO...........
"""

REPAIR = """
    ..................................O.....
    ........O.......................OOO.OOO.
    .......OOOO....................OO......O
    ..O...O...OO.OO...........O...O..O...OO.
    .OOOO.....O..OO..........OOOO...........
    O...O.......O..O........O...O...........
    .O.O..O..................O.O..O.........
    .....O.......................O..........
"""

SHOOTER = """
    OO............OO..O....OO..OO.............
    OO............O.OO......OO.OO.............
    ...............O......O.O.................
    ...............OOO....OO..................
    ..........................................
    ...............OOO....OO..................
    ...............O......O.O.................
    OO............O.OO......OO................
    OO............OO..O....OO.................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ...............................OOO...OOO..
    ..............................O...O.O...O.
    .............................O...OO.OO...O
    .............................O.OO.....OO.O
    ...............................O.......O..
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ..........................................
    ...............................OO.....OO..
    ...............................OO.....OO..
"""
