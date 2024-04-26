import platform
import subprocess
import getpass
import os



def clear_screen() -> None:
    """Platform independent clear screen"""
    # os.system("cls") if platform.uname().system == "Windows" else os.system("clear")
    subprocess.run("cls") if platform.uname().system == "Windows" else subprocess.run("clear")


def get_input(message) -> list[str]:
    """Return a list of string without trailing white space"""
    return input(message).strip().split()


def find_redirect_out_op(commands) -> int:
    for i in range(len(commands)):
        if commands[i] == ">":
            return i
        elif commands[i] == "<":
            return i
        elif commands[i] == "|":
            return i
    return -1


def change_directory(commands):
    try:
        if len(commands) > 1:
            os.chdir(commands[1])
        else:
            os.chdir(f"/home/{getpass.getuser()}")
    except FileNotFoundError as fnf:
        print(f"Directory not found: {fnf.filename}")
    except PermissionError as pe:
        print(f"Not sufficient permission: {pe.filename}")
    except NotADirectoryError as nae:
        print(f"Not a directory: {nae.filename}")


def shell_start_message() -> str:
    cwd = os.getcwd().split("/")
    for i in range(len(cwd) - 1):
        if len(cwd[i]) == 0:
            continue
        cwd[i] = cwd[i][0]
    cwd_s = "/".join(cwd)
    if cwd_s == f"/h/{getpass.getuser()}":
        return f"[{getpass.getuser()}@{platform.node()} ~/] ~> "
    return f"[{getpass.getuser()}@{platform.node()} {cwd_s}] ~> "
