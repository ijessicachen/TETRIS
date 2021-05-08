import curses

"""
GENERAL NOTES
9609 will be the general cell
"""

#Tetrominos
#def tetrominos(stdscr):


def tetris(stdscr):
  curses.curs_set(False)

  curses.color_pair(1)

  #TRIAL(?) TETROMINOS
  #Square
  stdscr.addstr(2, 3, chr(9609))
  stdscr.addstr(2, 5, chr(9609))
  stdscr.addstr(3, 3, chr(9609))
  stdscr.addstr(3, 5, chr(9609))
  #Line
  stdscr.addstr(5, 3, chr(9609))
  stdscr.addstr(5, 5, chr(9609))
  stdscr.addstr(5, 7, chr(9609))
  stdscr.addstr(5, 9, chr(9609))
  #L1
  stdscr.addstr(2, 13, chr(9609))
  stdscr.addstr(2, 15, chr(9609))
  stdscr.addstr(2, 17, chr(9609))
  stdscr.addstr(3, 17, chr(9609))
  #L2
  stdscr.addstr(4, 13, chr(9609))
  stdscr.addstr(5, 13, chr(9609))
  stdscr.addstr(5, 15, chr(9609))
  stdscr.addstr(5, 17, chr(9609))
  #Z1
  stdscr.addstr(2, 21, chr(9609))
  stdscr.addstr(2, 23, chr(9609))
  stdscr.addstr(3, 23, chr(9609))
  stdscr.addstr(3, 25, chr(9609))
  #Z2
  stdscr.addstr(5, 21, chr(9609))
  stdscr.addstr(5, 23, chr(9609))
  stdscr.addstr(4, 23, chr(9609))
  stdscr.addstr(4, 25, chr(9609))
  #T
  stdscr.addstr(3, 29, chr(9609))
  stdscr.addstr(3, 31, chr(9609))
  stdscr.addstr(4, 31, chr(9609))
  stdscr.addstr(3, 33, chr(9609))
  
  stdscr.getch()

curses.wrapper(tetris)
