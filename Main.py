from DATA.Game import IsRunning , while_running , clear_screen , show_cursor
import sys


if __name__ == "__main__":
    while IsRunning :
        clear_screen()
        try:
            while_running()
        except KeyboardInterrupt:
            pass
        finally:
            show_cursor()
            sys.stdout.write("\nВихід.\n")
            sys.stdout.flush()