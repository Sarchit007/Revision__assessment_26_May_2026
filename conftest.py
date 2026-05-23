import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from config.env import ConfigReader
from time import sleep


@pytest.fixture(scope="session")
def setup_and_teardown():
    ## Read the env and config file
    config = ConfigReader.read_config()
    env = config["qa"]          ## accessing the YAML file
    base_url = env["base_url"]

    # setup (for tsting )
    o = Options()

    o.add_argument("--no-sandbox")
    o.add_argument("--disable-notifications")
    o.add_argument("--start-maximized")

    driver = uc.Chrome(
        options=o,
        version_main=147,
        use_subprocess=True
    )

    driver.get(base_url)    ## opening the website in the .env file
    driver.maximize_window()
    # sleep(3)
    yield driver

    #Teardown began after here
    # driver.quit()
    input("Press Enter to close browser...")

    try:
        driver.quit()
    except:
        pass