from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.ixigo.com/?loginVisible=true")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, '(//button[text()="Log in/Sign up"])[1]').click()
sleep(5)

btn=driver.find_element(By.XPATH, '//div[@id="googleLogin"]')
action=webdriver.ActionChains(driver)
action.move_to_element(btn).perform()
action.click(btn).perform()