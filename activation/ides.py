from __future__ import annotations
import fnmatch
import json
import platform
from pathlib import Path

import pyperclip
from colorama import Fore


def is_ide_exists(folders: list[str], ide_name: str) -> bool:
    """
    Checks if any folder name in the given list contains the specified IDE name.

    This function searches through the list of folder names and checks if any of them
    match the specified IDE name in a case-insensitive manner. If a match is found,
    the folder is removed from the list.

    Args:
        folders (list[str]): A list of folder names to search.
        ide_name (str): The name of the IDE to search for.

    Returns:
        bool: True if a folder matching the IDE name is found, False otherwise.
    """
    for i, folder_name in enumerate(folders):
        if fnmatch.fnmatchcase(folder_name.lower(), f"*{ide_name.lower()}*"):
            folders.pop(i)
            return True
    return False


def check_installed_ides_windows(keys: dict[str, str]) -> dict[str, str]:
    """
    Checks for installed IDEs in the default JetBrains directory on Windows.

    This function scans the JetBrains directory on Windows for installed IDEs and
    compares the folder names with the provided IDE names to find matches.

    Args:
        keys (dict[str, str]): A dictionary where keys are IDE names and values are associated keys.

    Returns:
        dict[str, str]: A dictionary of installed IDEs and their license keys.
    """
    base_path = Path("C:\\Program Files\\JetBrains\\")
    folders = [item.name for item in base_path.iterdir() if item.is_dir()]
    print(f"{Fore.YELLOW}Check ides in path: {base_path}")
    return {ide: key for ide, key in keys.items() if is_ide_exists(folders, ide)}


def check_installed_ides_macos(keys: dict[str, str]) -> dict[str, str]:
    """
    Checks for installed IDEs in the default JetBrains directory on macOS.

    This function scans the Applications directory on macOS for installed IDEs and
    compares the folder names with the provided IDE names to find matches.

    Args:
        keys (dict[str, str]): A dictionary where keys are IDE names and values are associated keys.

    Returns:
        dict[str, str]: A dictionary of installed IDEs and their license keys.
    """
    base_path = Path("/Applications")
    folders = [item.name for item in base_path.iterdir() if item.is_dir()]
    print(f"{Fore.YELLOW}Check ides in path: {base_path}")
    return {ide: key for ide, key in keys.items() if is_ide_exists(folders, ide)}


def check_installed_ides(keys: dict[str, str]) -> dict[str, str]:
    """
    Determines which IDEs are installed based on the operating system.

    This function calls the appropriate function to check for installed IDEs depending
    on the operating system. It handles both Windows and macOS systems.

    Args:
        keys (dict[str, str]): A dictionary where keys are IDE names and values are associated keys.

    Returns:
        dict[str, str]: A dictionary of installed IDEs and their license keys.
    """
    os_type = platform.system()

    if os_type == "Windows":
        keys = check_installed_ides_windows(keys)
    elif os_type == "Darwin":  # macOS
        keys = check_installed_ides_macos(keys)
    print(f"{Fore.GREEN}Search ides in path complete")
    return keys


def show_keys_for_installed_ides(keys: dict[str, str]) -> None:
    """
    Displays a list of installed IDEs and allows the user to copy a key to the clipboard.

    This function displays the installed IDEs and their corresponding keys. The user
    can choose an IDE to copy its key to the clipboard or close the program.

    Args:
        keys (dict[str, str]): A dictionary where keys are IDE names and values are associated keys.

    Returns:
        None
    """
    installed_ides = check_installed_ides(keys)

    if not installed_ides:
        print(f"{Fore.RED}No IDEs found. All keys saved to keys.json")
        with (Path() / "keys.json").open("w") as file:
            json.dump(keys, file, indent=4, ensure_ascii=False)
        return

    print("\nSelect an IDE to copy its key:")
    for idx, ide in enumerate(installed_ides.keys(), 1):
        print(f"{idx}. {ide}")
    print(f"{len(installed_ides) + 1}. Close program")

    while True:
        choice = input("\nEnter your choice: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(installed_ides):
                ide = list(installed_ides.keys())[choice - 1]
                key = installed_ides[ide]
                pyperclip.copy(key)
                print(f"{Fore.GREEN}Key for {ide} copied to clipboard!")
            elif choice == len(installed_ides) + 1:
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please select a valid option.")
        else:
            print(f"{Fore.RED}Invalid input. Please enter a number.")
