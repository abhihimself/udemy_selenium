from selenium import webdriver
from base_layer import Selenium_base
import time

driver=webdriver.Firefox()
driver.get("https://letskodeit.teachable.com/p/practice")

servent=Selenium_base(driver)

locator="bmwradio"

element=servent.wait_for_element(locator,"id")
element.click()
time.sleep(5)
driver.quit()