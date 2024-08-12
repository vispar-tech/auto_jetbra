from colorama import init

from activation.activate import activate_jetbra
from activation.downloader import clear_temp, download_jetbra
from activation.driver import get_driver
from activation.get_mirror import get_mirror_link
from activation.ides import show_keys_for_installed_ides
from activation.message import (
    print_support_message,
    print_welcome_message,
)
from activation.parser import parse_jetbra_mirror

init(autoreset=True)


def main() -> None:
    print_welcome_message()
    driver = get_driver()

    mirror_link = get_mirror_link(driver)

    mirror_data = parse_jetbra_mirror(mirror_link)

    downloaded_file_path = download_jetbra(mirror_data["download_url"])

    activate_jetbra(downloaded_file_path)

    clear_temp(downloaded_file_path)

    show_keys_for_installed_ides(mirror_data["keys"])
    print_support_message()


if __name__ == "__main__":
    main()
