import curses
from curses import wrapper
import time

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    BLUE_AND_BLACK = curses.color_pair(1)
    WHITE_AND_RED = curses.color_pair(2)

    stdscr.clear()
    stdscr.refresh()

    max_y, max_x = stdscr.getmaxyx()

    if max_x < 58 or max_y < 12:
        stdscr.nodelay(True)
        for i in range(0, 10):
            stdscr.addstr(0,0,"Terminal too small! Please use a terminal bigger than 60x12. Exiting...", WHITE_AND_RED | curses.A_BLINK)
            stdscr.refresh()
            time.sleep(1)
        exit(1)

    elif max_x < 115:
        win1 = curses.newwin(12, 58, 2, (max_x - 58) // 2)
        header = """███╗   ███╗ █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██╔████╔██║███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
  ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗  
  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║  
  ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║  
  ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║  
  ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║  
  ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝  """
    else:
        win1 = curses.newwin(6, 115, 2, (max_x - 114) // 2)
        header = """███╗   ███╗ █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
██╔████╔██║███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝"""

    header = [char for char in header]
    for i in range(0, len(header)):
        win1.addstr(header[i], BLUE_AND_BLACK)
        win1.refresh()
        time.sleep(0.0007)

    win2 = curses.newwin(15, 45, 20, (max_x - 34) // 2)

    startup_display = [
        "1. Enter student's information.",
        "2. Enter course's information.",
        "3. Add course to existing student.",
        "4. Show all students data.",
        "5. Show all Courses.",
        "6. Show all student from a Course.",
        "7. Add marks for a student in a given course.",
        "8. Display marks for a given course.",
        "9. Show student GPA.",
        "10. Rank student's GPA.",
        '"exit" to quit the program.'
    ]

    option = 0
    while True:
        
        win2.clear()
        for i in range(0, len(startup_display)):
            if option == i:
                win2.addstr(i, 0, startup_display[i], curses.A_BLINK | BLUE_AND_BLACK)
            else:
                win2.addstr(i, 0, startup_display[i])
        win2.refresh()

        key = stdscr.getkey()
        if key == "KEY_UP":
            option -= 1 if option >= 1 else 0
        elif key == "KEY_DOWN":
            option += 1 if option < 10 else 0
        elif key in ['\n', '\r', curses.KEY_ENTER]:
            if option == 10:
                exit(1)
            if option == 0:
                print("Hello world")
    # Wait for a key press
    stdscr.getch()



# Example usage
wrapper(main)
