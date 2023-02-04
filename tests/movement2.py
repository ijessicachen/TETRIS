# ROTATION
'''
TO DO
* stage 1 *
- draw all tetrominoes 
- rotate them with arrow keys
- make rotation more efficient

***
CURRENTLY:
    - make tetrominoes in all rotation positions
      on grids
    - from there make a way to rotate them efficiently
    - when rotation also have an arrow on the screen 
      pointing to the rotation stage the top row is at
***

* stage 2 *
- below stage 1, DO NOT delete stage 1
- draw the tetrominos falling (as
  in movement1
- rotate them as they fall
- ensure that they land properly (no 
  floating, no through the ground)

goal of this is to deal with rotation, first while 
stationary, then while falling. 
'''

import curses

#tetrinominos
ch = chr(9609)
tShapes = ['O', 'I', 'L', 'J', 'Z', 'S', 'T']
tColours = [15, 228, 28, 210, 11, 2, 64]

# Initialize all units for all tetrominoes.
def init_mino_yxs(shape):

    # get the index of the given type.
    index = tShapes.index(shape)

    if index == 0:
        # O
        return [ [2, 12], [2, 14], [3, 12], [3, 14] ]
    elif index == 1:
        # I
        return [ [3, 20], [3, 22], [3, 24], [3, 26] ]
    elif index == 2:
        # L
        return [ [3, 32], [3, 34], [3, 36], [2, 36] ]
    elif index == 3:
        # J
        return [ [2, 42], [3, 42], [3, 44], [3, 46] ]
    elif index == 4:
        # Z
        return [ [2, 52], [2, 54], [3, 54], [3, 56] ]
    elif index == 5:
        # S
        return [ [3, 62], [3, 64], [2, 64], [2, 66] ]
    else:
        # T
        return [ [3, 72], [3, 74], [2, 74], [3, 76] ]


def init_colours(bg = -1):
    #Setting up colours
    curses.start_color()
    curses.use_default_colors()

    """
     refer to note in movement1.py
    """ 
    for i in range(0, curses.COLORS):
        #inialize colour pair
        if i == 15:
            curses.init_pair(i+1, i, 1)
        elif i == 16:
            curses.init_pair(i+1, i, 196)
        else:
            curses.init_pair(i+1, i, -1)

# Paint the tetrimino for the given mino variable and mino type.
#there's also an option to erase the mino
''' you can probably think of an intuitive way to combine
    this and the yx function '''
def paint_mino(stdscr, mino, shape, key, erase=False):

    c = tColours[shape]

    # using the python ternary operator to decide
    # what character to use for painting each unit.
    unit_ch = ' ' if erase else ch

    for unit in mino:
        if erase:
          stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(c))
        else:
          stdscr.addstr(unit[0]+1, unit[1], unit_ch, curses.color_pair(c))
          unit[0] += 1 #then change the actual value of the mino unit

# rotate the tetromino
#FOR NOW only rotate in one direction
def rotate (stdscr, mino, shape, key):

    #get the colour
    c = tColours[shape]

    #rotate
    '''
    for i in range (0, 4):
        switch (shape):
            case 6:
                
                break;
    '''



def tetris (stdscr):
    #bye bye cursor
    curses.curs_set(0)
    #nodelay mode
    stdscr.nodelay(True)
    #time of each loop? default time before refresh?
    stdscr.timeout(500)

    #colours
    bg = -1;
    init_colours(bg)

    #tetrominoes
    tetrominoes = []
    #initial positions
    for t in tShapes:
        index = tShapes.index(t)
        colour = tColours[index]
        mino = init_mino_yxs(t)
        tetrominoes.append(mino)
        paint_mino(stdscr, mino, tShapes.index(t), 0, erase = False)

    rotatepos(stdscr)

    while True:
        key = stdscr.getch()
        if key == ord('q') or key == 27:
            break

#I need a better idea of what the rotation will look like
''' hardcoded (•́⍜•̀) '''
def rotatepos (stdscr):

    #frames of reference for the rotations
    for n in range (7, 27, 5):
        #tetrominoes (•́⍜•̀)
        tetrominoes = []
        for t in tShapes:
            index = tShapes.index(t)
        #    colour = tColours[index]
            mino = init_mino_yxs(t)
            tetrominoes.append(mino)
            paint_mino(stdscr, mino, tShapes.index(t), 0, erase = False)
        
        #grids
        for i in range(32, 82, 10):   
            sGrid = [[n, i], [n, i+2], [n, i+4],
                     [n+1, i], [n+1, i+2], [n+1, i+4],
                     [n+2, i], [n+2, i+2], [n+2, i+4]]
            for unit in sGrid:
                stdscr.addstr(unit[0], unit[1], ch)

    #special case for the stick
    for n in range (6, 26, 5):
        i = 20
        sGrid = [[n+0, i], [n+0, i+2], [n+0, i+4], [n+0, i+6],
                 [n+1, i], [n+1, i+2], [n+1, i+4], [n+1, i+6],
                 [n+2, i], [n+2, i+2], [n+2, i+4], [n+2, i+6],
                 [n+3, i], [n+3, i+2], [n+3, i+4], [n+3, i+6]]
        for unit in sGrid:
            stdscr.addstr(unit[0], unit[1], ch)


curses.wrapper(tetris)

