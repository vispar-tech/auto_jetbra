from __future__ import annotations
from typing import TYPE_CHECKING

from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

if TYPE_CHECKING:
    from selenium import webdriver


def get_mirror_link(driver: webdriver.Chrome) -> str:
    """
    Retrieves the mirror link for activation from a specified website using Selenium WebDriver.

    This function navigates to a mirror checker website, waits for the results to be loaded,
    and then finds an available mirror link for activation. The first valid link found is returned.

    Args:
        driver (webdriver.Chrome): An instance of Selenium WebDriver for Chrome.

    Returns:
        str: The URL of the mirror link found for activation.

    Raises:
        Exception: If no online mirror is found or if no valid link is retrieved.

    Example:
        >>> from selenium import webdriver
        >>> driver = webdriver.Chrome()
        >>> mirror_link = get_mirror_link(driver)
        >>> print(mirror_link)
    """
    try:
        driver.get("https://3.jetbra.in/")

        # Wait until the results element is present on the page
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "checker.results")))

        # Wait until at least one online mirror is available
        WebDriverWait(driver, 30).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "#checker\\.results div.Node.online")) > 0,
        )

        nodes = driver.find_elements(By.CSS_SELECTOR, "#checker\\.results div.Node.online")

        if not nodes:
            msg = "Not found any online mirror for activation"
            raise Exception(msg)

        link = None
        for node in nodes:
            link = node.find_element(By.TAG_NAME, "a").get_attribute("href")  # type: ignore
            if link is not None:
                print(f"{Fore.GREEN}Mirror link found: {link}")
            break

        if link is None:
            msg = f"{Fore.RED}Not found mirror link to parse"
            raise Exception(msg)
        return link
    finally:
        driver.quit()
