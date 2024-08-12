from __future__ import annotations
from typing import TYPE_CHECKING

from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

if TYPE_CHECKING:
    from selenium import webdriver


def get_mirror_link(driver: webdriver.Chrome) -> str:
    try:
        driver.get("https://3.jetbra.in/")

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "checker.results")))

        WebDriverWait(driver, 30).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "#checker\\.results div.Node.online")) > 0,
        )

        nodes = driver.find_elements(By.CSS_SELECTOR, "#checker\\.results div.Node.online")

        if not nodes:
            msg = "Not found any online mirror for activation"
            raise Exception(msg)

        link = None
        for node in nodes:
            link = node.find_element(By.TAG_NAME, "a").get_attribute("href")
            if link is not None:
                print(f"{Fore.GREEN}Mirror link found: {link}")
            break

        if link is None:
            msg = f"{Fore.RED}Not found mirror link to parse"
            raise Exception(msg)
        return link
    finally:
        driver.quit()
