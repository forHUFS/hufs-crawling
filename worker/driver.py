import pathlib

from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by      import By
from selenium.webdriver.support.ui     import WebDriverWait
from selenium.webdriver.support        import expected_conditions as EC
from selenium.common.exceptions        import TimeoutException


class DriverUtils:
    def driver_wait(self, time = 2):
        wait = WebDriverWait(self.driver, time)

        return wait


    def wait_until_clickable_by_xpath(self, xpath):
        try:
            return True if self.driver_wait().until(
                EC.EC.element_to_be_clickable(By.XPATH, xpath)
            ) else False
        
        except TimeoutError:
            return False

    
    def wait_until_clickable_by_selector(self, selector):
        try:
            return True if self.driver_wait().until(
                EC.element_to_be_clickable(By.CSS_SELECTOR, selector)
            ) else False

        except TimeoutException:
            return False

    
    def wait_until_clickable_by_class_name(self, class_name):
        try:
            return True if self.driver_wait().until(
                EC.element_to_be_clickable(By.CLASS_NAME, class_name)
            ) else False
        
        except TimeoutException:
            return False

    
    def get_element_by_xapth(self, xpath):
        if self.wait_until_clickable_by_xpath(xpath):
            element = self.find_element_by_xpath(xpath)        
            return element
        
        else:
            return None

    
    def get_elements_by_xapth(self, xpath):
        if self.wait_until_clickable_by_xpath(xpath):
            elements = self.find_elements_by_xpath(xpath)
            return elements
        
        else:
            return None


    def get_element_by_css_selector(self, selector):
        if self.wait_until_clickable_by_selector(selector):
            element = self.find_element_by_css_selector(selector)
            return element

        else:
            return None

    def get_elements_by_css_selector(self, selector):
        if self.wait_until_clickable_by_selector(selector):
            elements = self.find_elements_by_css_selector(selector)
            return elements

        else:
            return None

    def get_element_by_class_name(self, class_name):
        if self.wait_until_clickable_by_class_name(class_name):
            element = self.find_element_by_class_name(class_name)
            return element
        
        else:
            return None

    def get_elemets_by_class_name(self, class_name):
        if self.wait_until_clickable_by_class_name(class_name):
            elements = self.find_elements_by_class_name(class_name)
            return elements

        else:
            return None


class WebDriver(webdriver.Chrome, DriverUtils):
    def __init__(self, file: str = 'chromedriver'):
        path = pathlib.Path(file).absolute()
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-sage')

        webdriver.Chrome.__init__(
            self,
            executable_path = path,
            options         = options
        )

    