import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class Selenium_base():
    def __init__(self,driver):
        self.driver=driver

    def ByType(self,locatorType):
        #simply takes locator type from user and return the relevant By class
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False



    def wait_for_element(self,locator,locatortype,timeout=10,pollfrequency=0.5):
        bytype=self.ByType(locatortype)
        wait=WebDriverWait(self.driver,timeout,poll_frequency=pollfrequency,
                           ignored_exceptions=[NoSuchElementException,
                                            ElementNotVisibleException,
                                            ElementNotSelectableException])
        try:
            element=None
            element=wait.until(EC.element_to_be_clickable((bytype,locator)))
            return element
        except:
            print("element not found")
            traceback.print_stack()
            return element




