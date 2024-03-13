import subprocess
from run_commands import (
    run_command,
    run_command_redirected
)
from utilities import (
    change_directory,
    clear_screen,
    get_input,
    shell_start_message,
    find_redirect_out_op,
)

clear_screen()
while True:
    shell_start = shell_start_message()
    data = get_input(message=shell_start)
    if data[0] == "cd":
        change_directory(data)
    elif find_redirect_out_op(commands=data) == -1:
        run_command(commands=data)
    else:
        run_command_redirected(commands=data)
