import os
import platform


def clear_screen():
    os.system("cls") if platform.uname(
    ).system == "Windows" else os.system("clear")


def find_item_in_list(itemToFind, listToSearch, caseInsensitive) -> int:
    if caseInsensitive == 1:
        itemToFind = itemToFind.upper()
        for i in range(0, len(listToSearch)):
            if (
                listToSearch[i].get_name().upper() == itemToFind
                or listToSearch[i].get_id().upper() == itemToFind
            ):
                return i
    else:
        for i in range(0, len(listToSearch)):
            if (
                listToSearch[i].get_name() == itemToFind
                or listToSearch[i].get_id() == itemToFind
            ):
                return i
    return -1


def find_in_list(itemToFind, listToSearch) -> int:
    for i in range(0, len(listToSearch)):
        if itemToFind == listToSearch[i]:
            return i
    return -1


def output_padding(item) -> str:
    tab_width = 20
    return " " * (tab_width - len(str(item)))
