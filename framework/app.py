from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


class App(object):
    # define the global timeout setting for waiting for page elements
    _timeout = 10
    
    # initializes the class, web driver object and error log
    def __init__(self, web_driver):
        super().__init__()
        self._driver = web_driver
        self._log = Log('error.log')
        self._log.Write('Debug log created')
        
    # navigates to a defined url
    def open(self, url):
        self._driver.get(url)
        
    # checks existence of element by class name
    def element_exists_by_class_name(self, class_name):
        try:
            element = WebDriverWait(self._driver, App._timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
            return True
        except Exception as e:
            self._log.Write('Error: ' + str(e))
            return False
        
    # checks existence of element by class name
    def element_exists_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self._driver, App._timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except Exception as e:
            self._log.Write('Error: ' + str(e))
            return False
        
    # checks existence of element by id
    def element_exists_by_id(self, id):
        try:
            element = WebDriverWait(self._driver, App._timeout).until(
                EC.visibility_of_element_located((By.ID, id)))
            return True
        except Exception as e:
            self._log.Write('Error: ' + str(e))
            return False
        
    # checks existence of generic page elements on the page to verify successful page load
    def key_page_elements_exist(self):
        if (self.element_exists_by_class_name('color_logo') and self.element_exists_by_class_name(
                'mainContainer') and self.element_exists_by_class_name('search')):
            return True
        else:
            self._log.Write('Error: All page elements are not displayed as expected')
            return False
        
    # selects a defined category from the main navigation bar
    def select_category_from_nav_bar(self, category):
        try:
            element = self._driver.find_element_by_xpath('//div[contains(@class, "navigation")]//a[contains(@text(), ' + category + ')]')
            element.click()
        except Exception as e:
            self._log.Write('Error: ' + str(e))
            
    # selects a defined article on page based on the article number
    def select_article_by_number(self, article_number):
        try:
            page_state = ''
            while page_state != 'complete': 
                time.sleep(1)
                page_state = str(self._driver.execute_script('return document.readyState;'))
            articles = self._driver.find_elements_by_xpath('//div[contains(@class, "post")]/*/h4/a')
            list_index = (article_number - 1)
            articles[list_index].click()
        except Exception as e:
            self._log.Write('Error: ' + str(e))
            
    # verifies successful page load
    def verify_page_load(self):
        page_state = str(self._driver.execute_script('return document.readyState;'))
        assert page_state == 'complete' and self.key_page_elements_exist(), 'Error verifying home page load'
        
    # verifies page load time is under a defined threshold
    def verify_page_load_time(self, threshold):
        loadtime = self._driver.execute_script(
            'return performance.timing.loadEventEnd - performance.timing.navigationStart;')
        assert loadtime <= threshold, "Error: page load taking too long: " + str(loadtime)
        
    # verifies that the author name is populated on article page
    def verify_author_name_populated(self):
        page_title = self._driver.find_element_by_tag_name("title").text
        author_name = self._driver.find_element_by_xpath('//div[contains(@class, "contact_box auth_named_desc")]/span')
        assert  len((author_name.text.strip())) > 0, "Author name not populated in article: " + page_title
    
    # quits browser
    def quit_browser(self):
        try:
            self._driver.quit()
        except Exception as e:
            self._log.Write('Error: ' + str(e))

# Log class handles writing error messages to a log file
class Log(object):
    
    def __init__(self, file):
        self.logfile = open(file, "w+")
        
    # writes message to error log
    def Write(self, msg):
        time = f'{datetime.datetime.now():%d/%m/%Y %H:%M:%S%z}'
        self.logfile.write('[' + str(time) + ']' + msg + '\n')









