import subprocess
from utilities import (
    find_redirect_out_op
)


def run_command(commands) -> None:
    """Run commands"""
    if len(commands) == 1 and commands[0] == "exit":
        exit(0)
    try:
        subprocess.run(commands, check=True)
    except FileNotFoundError:
        data_s = " ".join(commands)
        print(f"Unknown command: {data_s}")
    except subprocess.CalledProcessError as unknown_err_code:
        data_s = " ".join(commands)
        print(f'Command "{data_s}" returned non-zero exit status {unknown_err_code.returncode}')


def run_command_redirected(commands) -> None:
    """Run command with redirected input or output"""
    file_position = find_redirect_out_op(commands)
    try:
        if commands[file_position] == ">":
            commands.remove(">")
            with open(commands[file_position], "w") as f_out:
                subprocess.run(commands[:-1], check=True, stdout=f_out)
        elif commands[file_position] == "<":
            commands.remove("<")
            with open(commands[file_position], "r") as f_in:
                subprocess.run(commands[:-1], check=True, stdin=f_in)
        elif commands[file_position] == "|":
            subprocess.run(" ".join(commands), check=True, shell=True)
    except FileNotFoundError as not_found:
        print(f"Unknown command: {not_found.filename}")
    except subprocess.CalledProcessError as unknown_err_code:
        data_s = " ".join(commands)
        print(f'Command "{data_s}" returned non-zero exit status {unknown_err_code.returncode}')
    except IOError:
        print(f"Cannot create file {commands[file_position]}")
    except IndexError:
        print(f"Error: Missing arguments")
