from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IxigoPage(BasePage):


    login = (By.XPATH, '//button[. = "Log in/Sign up"]')
    google_btn = (By.XPATH, '(//div[@id="googleLogin"])[1]')
    gmail_text_area = (By.XPATH, '//input[@type="email"]')
    gmail_next = (By.XPATH, '//span[.="Next"]')
    password_text_area = (By.XPATH, '//input[@type="password"]')
    password_next = (By.XPATH,'//span[.="Next"]')
    continue_after_pass = (By.XPATH, '//span[.="Continue"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_loginn(self):
        self.click(self.login)


    def click_google(self):
        self.direct_click(self.google_btn)

    def switch_window(self):
        self.switch_latest_window()

    def text_for_gmail(self, gmail_text_area):
        self.enter_text(self.gmail_text_area, gmail_text_area)

    def click_next(self):
        self.click(self.gmail_next)

    def text_for_password(self, password_text_area):
        self.enter_text(self.password_text_area, password_text_area)

    def click_password_next(self):
        self.click(self.password_next)

    def click_continue(self):
        self.click(self.continue_after_pass)

    def return_original_window(self):
        self.switch_to_fisrt_window()









