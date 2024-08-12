from __future__ import annotations
import fnmatch
import json
import platform
from pathlib import Path

import pyperclip
from colorama import Fore


def is_ide_exists(folders: list[str], ide_name: str) -> bool:
    """
    Check what part of `ide_name` exists in user application folder.

    Args:
    ----
        folders (list[str]): _description_
        ide_name (str): _description_

    """
    for i, folder_name in enumerate(folders):
        if fnmatch.fnmatchcase(folder_name.lower(), f"*{ide_name.lower()}*"):
            folders.pop(i)
            return True
    return False


def check_installed_ides_windows(keys: dict[str, str]) -> dict[str, str]:
    base_path = Path("C:\\Program Files\\JetBrains\\")
    folders = [item.name for item in base_path.iterdir() if item.is_dir()]
    print(f"{Fore.YELLOW}Check ides in path: {base_path}")
    return {ide: key for ide, key in keys.items() if is_ide_exists(folders, ide)}


def check_installed_ides_macos(keys: dict[str, str]) -> dict[str, str]:
    base_path = Path("/Applications")
    folders = [item.name for item in base_path.iterdir() if item.is_dir()]
    print(f"{Fore.YELLOW}Check ides in path: {base_path}")
    return {ide: key for ide, key in keys.items() if is_ide_exists(folders, ide)}


def check_installed_ides(keys: dict[str, str]) -> dict[str, str]:
    os_type = platform.system()

    if os_type == "Windows":
        keys = check_installed_ides_windows(keys)
    if os_type == "Darwin":  # macOS
        keys = check_installed_ides_macos(keys)
    print(f"{Fore.GREEN}Search ides in path complete")
    return keys


def show_keys_for_installed_ides(keys: dict[str, str]) -> None:
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
