from config.env import ConfigReader
from pages.ixigo_page import IxigoPage
from time import sleep

from pages.travel_pages import TravelPage


def test_login_ixigo(setup_and_teardown):
    driver = setup_and_teardown

    ixp = IxigoPage(driver)
    tpp = TravelPage(driver)

    # reading data from config file
    config = ConfigReader.read_config()
    env = config['qa']

    BASE_URL = env['base_url']
    USER_EMAIL = env['user_email']
    USER_PASSWORD = env['password']
    FROM_CITY = env['from_city']



    # ixp.click_close()

    ixp.click_loginn()
    sleep(2)
    ixp.click_google()

    ixp.switch_window()
    sleep(3)

    ixp.text_for_gmail(USER_EMAIL)

    ixp.click_next()
    sleep(2)

    ixp.text_for_password(USER_PASSWORD)

    ixp.click_password_next()

    sleep(10)

    try:
        ixp.click_continue()
        sleep(2)
    except:
        pass

    ixp.return_original_window()

    sleep(2)
