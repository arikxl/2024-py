import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr(1,5, "hello world!")
    stdscr.refresh()
    stdscr.getkey()


wrapper(main)

https://www.youtube.com/watch?v=NQ5i1kJAA6Y
