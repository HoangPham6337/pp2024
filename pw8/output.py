import curses
import time

def exit_curses(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


def compatibility_check(window, max_y, max_x, warning_color):
    if max_x < 120 or max_y < 32:
        message = f"Current size: {max_x} x {max_y}. "
        message += "Please use a terminal bigger than 120x32."
        window.addstr(message, curses.A_BOLD)
        window.refresh()
        window.nodelay(True)
        warningWindow = curses.newwin(max_y, max_x, 1, 0)
        for i in range(0, 4):
            warningWindow.addstr(
                0, 0,
                "Terminal too small! Use compact UI",
                curses.color_pair(warning_color) | curses.A_BLINK
            )
            warningWindow.refresh()
            time.sleep(1)
        exit_curses(window)
        return True
    return False


def header_builder(window, header_color, max_x):
    headerWindow = curses.newwin(6, 115, 2, (max_x - 114) // 2)
    header = """███╗   ███╗ █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
██╔████╔██║███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝"""

    header = [char for char in header]
    for i in range(0, len(header)):
        headerWindow.addstr(header[i], curses.color_pair(header_color))
        headerWindow.refresh()
        time.sleep(0.001)


def message_builder(window, message_color, max_x):
    boxWindow = curses.newwin(9, 120, 10, (max_x - 120) // 2)
    boxWindow.attron(curses.color_pair(message_color))
    boxWindow.box()
    boxWindow.refresh()

    messageWindow = curses.newwin(7, 118, 11, (max_x - 118) // 2)
    message1 = "Welcome to the Student Marks Management System,"
    message1 += " an interactive and user-friendly application designed to"
    message1 += " streamline   the process of managing and tracking student"
    message1 += " performance across various courses. This system is an ideal"
    message1 += " tool for     educational institutions, teachers,"
    message1 += " and administrative staff who"
    message1 += " seek an efficient way to handle academic records."
    message2 = "\n\nUpon launching the Student Marks Management System,"
    message2 += " you will be greeted with a main menu offering various"
    message2 += " options,    such as adding or viewing student information,"
    message2 += " managing courses, and recording marks. Navigate through"
    message2 += " these options  using the keyboard, and follow the on-screen"
    message2 += " prompts to input or retrieve data."
    messageWindow.addstr(message1)
    messageWindow.addstr(message2)
    messageWindow.refresh()
