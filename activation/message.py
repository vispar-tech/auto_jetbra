from colorama import Fore, Style


def print_base_message() -> None:
    print(f"{Fore.GREEN}Thank you for using the `JetBrains IDE Activation Script`!")
    print(f"{Fore.GREEN}I would be grateful if you could:")
    print(f"{Fore.CYAN}Subscribe to Telegram channel: https://t.me/vispar_journal")
    print(f"{Fore.CYAN}Check out GitHub: https://github.com/vispar-tech")


def print_support_message() -> None:
    art = """
  ████████ ██     ██ ███████  ███████    ███████   ███████   ██████████
 ██░░░░░░ ░██    ░██░██░░░░██░██░░░░██  ██░░░░░██ ░██░░░░██ ░░░░░██░░░
░██       ░██    ░██░██   ░██░██   ░██ ██     ░░██░██   ░██     ░██
░█████████░██    ░██░███████ ░███████ ░██      ░██░███████      ░██
░░░░░░░░██░██    ░██░██░░░░  ░██░░░░  ░██      ░██░██░░░██      ░██
       ░██░██    ░██░██      ░██      ░░██     ██ ░██  ░░██     ░██
 ████████ ░░███████ ░██      ░██       ░░███████  ░██   ░░██    ░██
░░░░░░░░   ░░░░░░░  ░░       ░░         ░░░░░░░   ░░     ░░     ░░
    """
    print("\n")
    print(f"{Fore.BLUE}{art}{Style.RESET_ALL}")
    print_base_message()


def print_welcome_message() -> None:
    art = """
      ██ ████████ ██████████ ██████   ███████       ██
     ░██░██░░░░░ ░░░░░██░░░ ░█░░░░██ ░██░░░░██     ████
     ░██░██          ░██    ░█   ░██ ░██   ░██    ██░░██
     ░██░███████     ░██    ░██████  ░███████    ██  ░░██
     ░██░██░░░░      ░██    ░█░░░░ ██░██░░░██   ██████████
 ██  ░██░██          ░██    ░█    ░██░██  ░░██ ░██░░░░░░██
░░█████ ░████████    ░██    ░███████ ░██   ░░██░██     ░██
 ░░░░░  ░░░░░░░░     ░░     ░░░░░░░  ░░     ░░ ░░      ░░
    """
    print(f"{Fore.BLUE}{art}{Style.RESET_ALL}")
    print_base_message()
    print("\n")
