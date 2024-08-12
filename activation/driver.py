from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver() -> WebDriver:
    print(f"{Fore.YELLOW}Initializing WebDriver...")
    service = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    chrome_version = driver.capabilities.get("browserVersion")  # type: ignore
    print(f"{Fore.BLUE}Chrome version in use: {chrome_version}")
    return driver
