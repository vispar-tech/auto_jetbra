from __future__ import annotations
import json
import re
from typing import TypedDict

from bs4 import BeautifulSoup, Tag
from colorama import Fore
from requests import Session, status_codes


class MirrorData(TypedDict):
    """
    Represents the data structure for parsed mirror information.

    Attributes:
        download_url (str): The URL to download `jetbra.zip`.
        keys (dict[str, str]): A dictionary of IDE titles and their license keys.
    """

    download_url: str
    keys: dict[str, str]


def parse_jetbra_mirror(mirror_url: str) -> MirrorData:
    """
    Parses the JetBra mirror page to extract download URL and IDE keys.

    This function fetches and parses the HTML content from the specified mirror URL. It
    extracts the download link for `jetbra.zip` and a dictionary of IDE keys from the script tag
    within the HTML. The IDE keys are mapped to their corresponding titles based on the
    mirror's content.

    Args:
        mirror_url (str): The URL of the JetBra mirror page to parse.

    Returns:
        MirrorData: A dictionary containing the download URL and IDE keys.

    Raises:
        Exception: If the HTTP request fails or the expected elements are not found in the HTML.
        TypeError: If the expected types of the parsed elements are incorrect.
        ValueError: If there is an issue with parsing JSON or finding the necessary script or data.
    """
    session = Session()

    response = session.get(url=mirror_url, timeout=15)

    if response.status_code != status_codes.codes["ok"]:
        msg = f"Failed to fetch data from {mirror_url}"
        raise Exception(msg)

    soup = BeautifulSoup(response.content, "html.parser")

    # Parse `jetbra` download link
    download_link = soup.find("a", title="Download jetbra first")
    if not isinstance(download_link, Tag):
        msg = "Link with title='Download jetbra first' not found"
        raise TypeError(msg)

    download_url = download_link.get("href")
    if not isinstance(download_url, str):
        msg = f"Download link has wrong type, expected `str`, but found {type(download_url)}"
        raise TypeError(msg)

    # Parse jbkeys dictionary in script tag
    script_tag = soup.find("script", text=re.compile(r"let jbKeys = "))
    if not script_tag:
        msg = "Script tag containing jbKeys not found"
        raise ValueError(msg)

    script_text = script_tag.get_text()
    jbkeys_match = re.search(r"let jbKeys\s*=\s*({.*?});", script_text, re.DOTALL)
    if not jbkeys_match:
        msg = "jbKeys variable not found in the script tag"
        raise ValueError(msg)

    jbkeys_str = jbkeys_match.group(1)
    try:
        jbkeys = json.loads(jbkeys_str.replace("'", '"'))
    except json.JSONDecodeError as e:
        msg = "Error parsing jbKeys JSON"
        raise ValueError(msg) from e

    print(f"{Fore.GREEN}Parsing mirror completed")

    # Match licenses key to IDE title
    licenses = {}

    articles = soup.find_all("article", class_="card")

    for article in articles:
        data_sequence = article.get("data-sequence")

        button = article.find("button")
        data_version = button.get("data-version") if button else None

        h1 = article.find("h1", class_="truncate")
        title = h1.get("title") if h1 else None

        licenses[title] = jbkeys[data_sequence][data_version]
    return MirrorData({"download_url": mirror_url + download_url, "keys": licenses})
