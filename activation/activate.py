import platform
import subprocess
import zipfile
from pathlib import Path

from colorama import Fore


def activate_jetbra(file_path: Path) -> None:
    os_type = platform.system()

    extract_dir = file_path.with_suffix("")
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    install_script = None
    scripts_dir = extract_dir / "jetbra/scripts"

    if os_type == "Darwin":
        install_script = scripts_dir / "install.sh"
        print(f"{Fore.GREEN}Detected macOS. Running {install_script.name}...")
    elif os_type == "Windows":
        print(f"{Fore.GREEN}Detected Windows. Please choose the installation type:")
        print("1. For all users")
        print("2. For current user")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            install_script = scripts_dir / "install-all-users.vbs"
            print(f"{Fore.GREEN}Chosen installation for all users.")
        elif choice == "2":
            install_script = scripts_dir / "install-current-user.vbs"
            print(f"{Fore.GREEN}Chosen installation for current user.")
        else:
            print(f"{Fore.RED}Invalid choice.")
            return

    else:
        print(f"{Fore.RED}Unsupported operating system.")
        return

    if install_script and install_script.exists():
        try:
            if os_type == "Windows":
                subprocess.run(
                    ["cscript", str(install_script)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )
            else:
                subprocess.run(
                    ["bash", str(install_script)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )

            print(f"{Fore.GREEN}Successfully executed: {install_script.name}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error occurred while executing the script: {e}")
    else:
        print(f"{Fore.RED}Script not found: {install_script}")
