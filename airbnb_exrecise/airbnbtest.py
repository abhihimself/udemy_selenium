from selenium import webdriver

class Test_airbnb():
    def __init__(self):
        self.search_box="//input[@id='search-location']"
        self.check_in_date="//input[@id='startDate']"
        self.check_out_date="//input[@id='endDate']"
        self.guest_dropdown="//button[ @class ='GuestPickerTrigger__button']"
        self.guest_plus_button="//button[@class='button_1qfdqz3-o_O-button_1ju6z0l" \
                               "-o_O-button_small_1h534dv-o_O-button_light_1a24k02' " \
                               "and @aria-label='1 adult (+)']"
        self.submit_button="//button[@class='btn btn-primary btn-large btn-block' and @type='submit']"

        self.driver=webdriver.Firefox()
        self.driver.get("https://www.airbnb.co.in/")
        self.driver.implicitly_wait(10)



    def test_airbnb(self):
        search_b=self.find_element(self.search_box)
        search_b.send_keys("Maxico City")
        check_in=self.find_element(self.check_in_date)
        check_in.send_keys("12")
        check_out = self.find_element(self.check_out_date)
        check_out.send_keys("15")
        guest_number = self.find_element(self.guest_dropdown)
        guest_number.click()
        guest_number_plus=self.find_element(self.guest_plus_button)
        guest_number_plus.click()
        search_button=self.find_element(self.submit_button)
        search_button.click()

        self.driver.quit()


    def find_element(self,element):

        return self.driver.find_element_by_xpath(element)


t=Test_airbnb()
t.test_airbnb()