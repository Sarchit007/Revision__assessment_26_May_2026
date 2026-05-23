from config.env import ConfigReader

from time import sleep

from pages.travel_pages import TravelPage


def test_travel_ixigo(setup_and_teardown):
    driver = setup_and_teardown

    driver.refresh()
    sleep(2)

    tpp = TravelPage(driver)

    config = ConfigReader.read_config()
    env = config['qa']
    FROM_CITY = env['from_city']
    TO_CITY = env['to_city']

    tpp.click_from()
    sleep(2)
    tpp.enter_location(FROM_CITY)
    sleep(2)
    tpp.first_suggestion_click()
    sleep(2)

    # tpp.click_to()
    tpp.enter_to_location(TO_CITY)
    sleep(2)
    tpp.to_suggestion_click()
    sleep(2)

    tpp.calender_date()
    sleep(2)
    tpp.adult()
    sleep(2)
    tpp.click_done_button()
    sleep(2)
    # tpp.click_checkbox()
    tpp.search_click()

