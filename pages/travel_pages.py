from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TravelPage(BasePage):

    from_location = (By.XPATH, '(//div[contains(@class,"flex-1 h-full flex flex-col justify-center")])[1]')
    from_input = (By.XPATH, '//input[contains(@class,"placeholder:text-disabled")]')
    first_element = (By.XPATH, '(//div[contains(@class,"flex relative gap-10 items-center")])[14]')
    to_location = (By.XPATH, '(//span[text()="To"]/ancestor::div[contains(@class,"flex-1")])[2]')
    to_input = (By.XPATH, '(//input[contains(@class,"outline-none")])[2]')
    to_first_select = (By.XPATH, '(//div[contains(@class,"flex relative gap-10 items-center")])[24]')
    calendar = (By.XPATH, '(//button[contains(@class , "react-calendar__tile react")])[25]')
    adult_selection = (By.XPATH , '(//button[contains(@class , "py-1.5 px-2.5 rounded-10 bg")])[3]')
    adult_done_button = (By.XPATH, '//button[. = "Done"]')
    cancellation_checkbox = (By.XPATH, '//input[@type="checkbox"]')
    search = (By.XPATH, '//button[contains(. , "Search")]')



    def __init__(self, driver):
        super().__init__(driver)


    def click_from(self):
        self.click(self.from_location)

    def enter_location(self, from_location):
        self.enter_text(self.from_input, from_location)

    def first_suggestion_click(self):
        self.click(self.first_element)

    def click_to(self):
        self.direct_click(self.to_location)

    def enter_to_location(self, to_input):
        self.enter_text(self.to_input, to_input)

    def to_suggestion_click(self):
        self.click(self.to_first_select)

    def calender_date(self):
        self.click(self.calendar)

    def adult(self):
        self.click(self.adult_selection)

    def click_done_button(self):
        self.click(self.adult_done_button)

    def click_checkbox(self):
        self.click(self.cancellation_checkbox)

    def search_click(self):
        self.click(self.search)


