import math
from datetime import datetime
import curses


def get_input_as_string(prompt) -> str:
    while True:
        data = input(prompt).strip()
        if not data:
            print("Cannot leave input blank, please try again!")
        else:
            return data


def get_input_as_int(prompt) -> int:
    while True:
        data = input(prompt).strip()
        try:
            return int(data)
        except ValueError:
            print("Invalid input, please try again!")


def get_input_as_float(prompt) -> float:
    while True:
        data = input(prompt).strip()
        try:
            return float(data)
        except ValueError:
            print("Invalid input, please try again!")


def get_input_as_float_floor(prompt) -> int:
    while True:
        data = input(prompt).strip()
        try:
            return int(math.floor(float(data) / 20.0 * 10.0))
        except ValueError:
            print("Invalid input, please try again!")


def get_input_as_date(prompt) -> datetime:
    while True:
        date_str = get_input_as_string(prompt)
        try:
            date = datetime.strptime(
                date_str, "%d-%m-%Y").date().strftime("%d-%m-%Y")
            return date
        except ValueError:
            print("Invalid date input. Please use the format DD-MM-YYYY and try again!")


def get_input_as_int_curses(window, prompt, silent, limit):
    if not silent:
        window.clear()
        window.addstr(prompt, curses.A_BOLD)
        window.refresh()

    num_str = ""
    while True:
        # Return the unicode, not the literal string representation of key

        key = window.getch()
        # Ignore everything that not a number
        if key >= ord("0") and key <= ord("9"):
            if len(num_str) >= limit:
                continue
            num_str += chr(key)
            window.addstr(chr(key), curses.A_BOLD)
        elif key == curses.KEY_BACKSPACE or key == 127:
            if len(num_str) > 0:
                num_str = num_str[:-1]
                # Delete the number replace by space then delete the space
                window.addstr("\b \b")
        elif key in [10, "\n", "\r", curses.KEY_ENTER]:
            break
        window.refresh()

    return int(num_str) if num_str else 0
