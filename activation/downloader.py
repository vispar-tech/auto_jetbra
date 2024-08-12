from __future__ import annotations
import shutil
import tempfile
from pathlib import Path

import requests
from colorama import Fore


def download_jetbra(download_url: str) -> Path:
    try:
        temp_dir = Path(tempfile.mkdtemp())

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


def clear_temp(file_path: Path) -> None:
    shutil.rmtree(file_path.parent)
