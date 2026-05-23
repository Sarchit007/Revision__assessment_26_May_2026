from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   ## waiting time for element

    ## element to be clickable
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def direct_click(self, locator):
        self.driver.find_element(*locator).click()

    ## ENter text and clear
    def enter_text(self, locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    ## get text from the element
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    ## hovering over the element
    def hovering(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def action_enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).click().send_keys(text).perform()

    def switch_latest_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_fisrt_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


    def switch_frame(self, locator):
        frame = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(frame)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])



