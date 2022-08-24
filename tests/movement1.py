import curses

#tetrinominos
ch = chr(9609)
tShapes = ('O', 'I', 'L', 'J', 'Z', 'S', 'T')
tColours = (15, 228, 28, 210, 11, 2, 64)


# Paint the tetrimino for the given mino variable and mino type.
def paint_mino(stdscr, mino, type, key, erase=False):

    i = tShapes.index(type)
    c = tColours[i]

    # using the python ternary operator to decide
    # what character to use for painting each unit.
    unit_ch = ' ' if erase else ch

    for unit in mino:
        if erase == False:
          stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(c))
        else:
            # don't know why this is here, will remove it          if key == chr(32):
          stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(c))

# calculate the new yxs for the given mino, type and action.
def calc_mino_yxs(mino, type, action, key):

    new_mino = []
    maxY = 0
    out = False #as in if it's through the floor

    # work on the action: move down.
    for unit in mino:
        new_mino.append([unit[0]+1, unit[1]])
           
        #clearly none of the below is working so I'll just 
        #rework this part
        """
        if key == chr(25):
          new_mino.append([unit[0] + 2, unit[1]]);
        elif key == chr(32):
          new_mino.append([unit[0] - 1, unit[1]]);
        elif key == chr(-1):
          new_mino.append([unit[0] + 1, unit[1]]);
        """
        #if key == chr(-1):
        #if key == chr(32):
          #new_mino.append([unit[0]+(out-unit[0]-1), unit[1]])
        #else:
        """
        if key == chr(32):
          new_mino.append([unit[0] + 1, unit[1]])
        maxY = unit[0] if unit[0] >= maxY else maxY
        out = (maxY + 1) >= 15
        """

    return (new_mino, out)

# Initialize all units for all tetrominoes.
def init_mino_yxs(type):

    # get the index of the given type.
    index = tShapes.index(type)

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
   I'm guessing the if statement is to avoid messing it
   up like I did in the blocks.py. However, considering
   how it's kind of weirdly complicated, perhaps this 
   version is the wrong version. Even if that's the case,
   until I figure out what's right I will keep it this way
   since my other games use this colour set with these
   numbers.
  """ 
  for i in range(0, curses.COLORS):
      #inialize colour pair
      if i == 15:
          curses.init_pair(i+1, i, 1)
      elif i == 16:
          curses.init_pair(i+1, i, 196)
      else:
          curses.init_pair(i+1, i, -1)

"""
FIND OUT WHERE type (the variable) IS COMING FROM
"""
def tetris(stdscr):
  #bye bye cursor
  curses.curs_set(0)

  #nodelay mode
  stdscr.nodelay(True)
  stdscr.timeout(500)

  #colours
  bg = -1
  init_colours(bg)
  
  #floor
  for i in range(0, 78):
    stdscr.addch(15, 3+i, curses.ACS_HLINE, curses.color_pair(245))
  stdscr.getch()

  #tetrominoes
  tetrominoes = []
  #initial positions
  for t in tShapes: #list in the beginning naming types of tetr…
    index = tShapes.index(t)
    colour = tColours[index]
    mino = init_mino_yxs(t)
    tetrominoes.append(mino)
    paint_mino(stdscr, mino, t, 0)

  # I think the logic looks great, I just don't understand it, so 
  #it's time to just go line by line to try and figure out what's
  #going on
  # loop for movement
  while True:
    key = stdscr.getch()

    if key == ord('q'):
      break
    else:
    # all tetronimos will move one unit down
      #new coordinates for tetrominoes
      new_yxs, out = calc_mino_yxs(mino, type, 'MOVE_DOWN', key)
      #erase the current tetrominoes
      paint_mino(stdscr, mino, type, key, erase = True)
   

    """
      for mino in tetrominoes:
        index = tetrominoes.index(mino)
        colour = tColours[index]
        type = tShapes[index]

        #new coordinates for tetrominoes
        #new_yxs, out = calc_mino_yxs(mino, type, 'MOVE_DOWN', key)
        #erase the current tetrominoes
        paint_mino(stdscr, mino, type, key, erase = True)

        #check if they broke the floor
        #if out:
        #  new_yxs = init_mino_yxs(type)

        #The new tetromino
        #paint_mino(stdscr, new_yxs, type, key)
        #reset the new tetromino list
        #tetrominoes[index] = new_yxs
        """

curses.wrapper(tetris)
