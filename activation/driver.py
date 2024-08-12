from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver() -> WebDriver:
    """
    Initializes and returns a Chrome WebDriver instance.

    This function sets up a Chrome WebDriver instance with headless mode enabled.
    It uses the `webdriver_manager` package to automatically handle the ChromeDriver installation.

    Steps performed:
    1. Prints a message indicating the initialization of the WebDriver.
    2. Sets up a ChromeDriver service using `webdriver_manager`.
    3. Configures Chrome options to run in headless mode (no GUI).
    4. Initializes the WebDriver with the specified options.
    5. Prints the version of Chrome in use.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.

    Example:
        >>> driver = get_driver()
        >>> driver.get("http://example.com")
        >>> print(driver.title)
        Output -> 'Example Domain'

    Note:
        This function assumes that Chrome and ChromeDriver are compatible.
        The `webdriver_manager` package handles ChromeDriver installation and updates.

    """
    print(f"{Fore.YELLOW}Initializing WebDriver...")
    service = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # type: ignore

    driver = webdriver.Chrome(service=service, options=chrome_options)
    chrome_version = driver.capabilities.get("browserVersion")  # type: ignore
    print(f"{Fore.BLUE}Chrome version in use: {chrome_version}")
    return driver
