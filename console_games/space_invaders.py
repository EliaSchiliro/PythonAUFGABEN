
import curses
from time import sleep

def draw_game(stdscr):
    shell = curses.initscr()
    shell.nodelay(True)
    # diese var wird gefüllt mit der gedrückten taste
    k = 0
    # hole hoehe und breite des bildschirms
    height, width = stdscr.getmaxyx()
    #berechne start position des raumschiffes
    cursor_x = (width - (width % 2)) // 2


    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in cursesq
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):
        # hole mir die gedrückte taste
        k = stdscr.getch()
        # Initialization
        stdscr.clear()

        if k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        # stelle sicher das raumschiff nicht aus dem bildschirm fliegt


        # zeige die positionen an oben links
        whstr = "Width: {}, Height: {}, cursor_x: {}, key_pressed: {}".format(width, height, cursor_x, k)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))
        # render your starship
        stdscr.addstr(height-1, cursor_x, "X", curses.color_pair(1))

        #setze immer den cursor in die ecke damit er im spiel nicht stört
        stdscr.move(0, 0)



        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        sleep(1)


def main():
    curses.wrapper(draw_game)


if __name__ == "__main__":
    main()