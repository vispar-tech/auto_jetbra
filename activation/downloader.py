from __future__ import annotations
import shutil
from pathlib import Path

import requests
from colorama import Fore


def download_jetbra(download_url: str) -> Path:
    """
    Download a `jetbra` archive from the specified URL and saves it to a temporary directory.

    This function handles the download of a `jetbra.zip` from the given URL and stores it
    in a temporary directory. The file is saved with the name derived from the URL's
    last segment. The function handles errors during the download process and
    raises an exception if any error occurs.

    Args:
        download_url (str): The URL of the mirror `jetbra` archive

    Returns:
        Path: The path to the `jetbra.zip` file.

    Raises:
        Exception: If an error occurs during the download process.

    Example:
        >>> download_url = "https://example.com/file.zip"
        >>> file_path = download_jetbra(download_url)
        >>> print(file_path)
        /tmp/tmp12345/file.zip

    """
    try:
        temp_dir = Path().parent / "downloaded"
        temp_dir.mkdir(parents=True, exist_ok=True)

        if len(list(temp_dir.iterdir())):
            shutil.rmtree(temp_dir)
            temp_dir.mkdir(parents=True, exist_ok=True)

        local_filename = temp_dir / download_url.split("/")[-1]

        print(f"{Fore.YELLOW}Starting download: {local_filename.name}")

        response = requests.get(download_url, stream=True, timeout=60)

        with local_filename.open("wb") as file:
            file.write(response.content)

        print(f"{Fore.GREEN}Download completed: {local_filename.name}")

    except Exception as e:
        print(f"{Fore.RED}Error while download jetbra.zip occurred: {e}")
        raise
    else:
        return local_filename
