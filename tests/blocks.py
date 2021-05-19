import curses

"""
GENERAL NOTES
9609 will be the general cell
"""

#Tetrominos
#def tetrominos(stdscr):


def tetris(stdscr):
  #Setting up colours
  curses.start_color()
  curses.use_default_colors()
  #initializing
  for i in range(0, curses.COLORS):
    curses.init_pair(i+1, i-1, -1)

  #bye bye cursor
  curses.curs_set(0)

  #Test colour scheme
  stdscr.addstr(8, 3, chr(9609), curses.color_pair(16))
  stdscr.addstr(9, 3, chr(9609), curses.color_pair(228))
  stdscr.addstr(8, 5, chr(9609), curses.color_pair(23))
  stdscr.addstr(9, 5, chr(9609), curses.color_pair(210))
  stdscr.addstr(8, 7, chr(9609), curses.color_pair(12))
  stdscr.addstr(9, 7, chr(9609), curses.color_pair(11))
  stdscr.addstr(8, 9, chr(9609), curses.color_pair(59))

  #trial border 1
  stdscr.addstr(2, 41, chr(9698), curses.color_pair(245))
  for i in range(0, 8, 2):
    stdscr.addstr(2, 44+i, chr(10074), curses.color_pair(245))
  stdscr.addstr(2, 51, chr(9699), curses.color_pair(245))
  for i in range(6):
    stdscr.addstr(3+i, 51, chr(11052), curses.color_pair(245))
  stdscr.addstr(9, 51, chr(9700), curses.color_pair(245))
  for i in range(0, 8, 2):
    stdscr.addstr(9, 49-i, chr(10074), curses.color_pair(245))
  stdscr.addstr(9, 41, chr(9701), curses.color_pair(245))
  for i in range(6):
    stdscr.addstr(3+i, 41, chr(11052), curses.color_pair(245))
  #trial border 2
  for i in range(0, 12, 2):
    stdscr.addstr(2, 57+i, chr(9609), curses.color_pair(245))
  for i in range(6):
    stdscr.addstr(3+i, 67, chr(9609), curses.color_pair(245))
  for i in range(0, 12, 2):
    stdscr.addstr(9, 57+i, chr(9609), curses.color_pair(245))
  for i in range(6):
    stdscr.addstr(3+i, 57, chr(9609), curses.color_pair(245))

  #TRIAL(?) TETROMINOS
  #O
  stdscr.addstr(2, 3, chr(9609), curses.color_pair(16))
  stdscr.addstr(2, 5, chr(9609), curses.color_pair(16))
  stdscr.addstr(3, 3, chr(9609), curses.color_pair(16))
  stdscr.addstr(3, 5, chr(9609), curses.color_pair(16))
  #I
  stdscr.addstr(5, 3, chr(9609), curses.color_pair(228))
  stdscr.addstr(5, 5, chr(9609), curses.color_pair(228))
  stdscr.addstr(5, 7, chr(9609), curses.color_pair(228))
  stdscr.addstr(5, 9, chr(9609), curses.color_pair(228))
  #L
  stdscr.addstr(2, 13, chr(9609), curses.color_pair(23))
  stdscr.addstr(2, 15, chr(9609), curses.color_pair(23))
  stdscr.addstr(2, 17, chr(9609), curses.color_pair(23))
  stdscr.addstr(3, 13, chr(9609), curses.color_pair(23))
  #J
  stdscr.addstr(4, 13, chr(9609), curses.color_pair(210))
  stdscr.addstr(5, 13, chr(9609), curses.color_pair(210))
  stdscr.addstr(5, 15, chr(9609), curses.color_pair(210))
  stdscr.addstr(5, 17, chr(9609), curses.color_pair(210))
  #Z
  stdscr.addstr(2, 21, chr(9609), curses.color_pair(12))
  stdscr.addstr(2, 23, chr(9609), curses.color_pair(12))
  stdscr.addstr(3, 23, chr(9609), curses.color_pair(12))
  stdscr.addstr(3, 25, chr(9609), curses.color_pair(12))
  #S
  stdscr.addstr(5, 21, chr(9609), curses.color_pair(11))
  stdscr.addstr(5, 23, chr(9609), curses.color_pair(11))
  stdscr.addstr(4, 23, chr(9609), curses.color_pair(11))
  stdscr.addstr(4, 25, chr(9609), curses.color_pair(11))
  #T
  stdscr.addstr(3, 29, chr(9609), curses.color_pair(59))
  stdscr.addstr(3, 31, chr(9609), curses.color_pair(59))
  stdscr.addstr(4, 31, chr(9609), curses.color_pair(59))
  stdscr.addstr(3, 33, chr(9609), curses.color_pair(59))
  
  stdscr.getch()

curses.wrapper(tetris)