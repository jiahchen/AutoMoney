# -*- coding: utf-8 -*-
""" BasePage Classes """

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import signal
class BasePage(object):
    """ The basic page parent class """
    url = None
    timeout = 5
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, form_xpath, value):
        """ Find the element by css selector and send key to the element"""
        self.driver.find_element_by_xpath(form_xpath).send_keys(value)

    def navigate(self):
        """ Go the the page """
        self.driver.get(self.url)

    def click_element(self, form_xpath):
        """ Find the element by css selector and click the element"""
        self.driver.find_element_by_xpath(form_xpath).click()

    def wait_element_located(self, wait_time_limit, form_xpath):
        """ Wait for the element located """
        WebDriverWait(self.driver, wait_time_limit).until(EC.presence_of_element_located((By.XPATH, form_xpath)))

    def get_element_text(self, form_xpath):
        """ get element text """
        return self.driver.find_element_by_xpath(form_xpath).text

    def clear_element_text(self, form_xpath):
        """ clear text of element """
        self.driver.find_element_by_xpath(form_xpath).click()
        self.driver.find_element_by_xpath(form_xpath).send_keys(Keys.CONTROL+'a')
        self.driver.find_element_by_xpath(form_xpath).send_keys(Keys.DELETE)

    def is_element_exist(self, form_xpath):
        """ Check if the element exists"""
        try:
            self.driver.find_element_by_xpath(form_xpath)
            return True
        except NoSuchElementException:
            return False

    def wait_element_clickable(self, wait_time_limit, form_xpath):
        """ Wait for the element clickable """
        WebDriverWait(self.driver, wait_time_limit).until(EC.element_to_be_clickable((By.XPATH, form_xpath)))

    def wait_text_present_in_element(self, wait_time_limit, element_text, form_xpath):
        WebDriverWait(self.driver, wait_time_limit).until(EC.text_to_be_present_in_element((By.XPATH, form_xpath), element_text))

    def get_element_attribute(self, form_xpath, attribute):
        """ get element attribute """
        return self.driver.find_element_by_xpath(form_xpath).get_attribute(attribute)

    def set_url(self, url):
        """ Set url """
        self.url = url

    def close_page(self):
        """ close the browser """
        self.driver.close()

    def quit_driver(self):
        self.driver.service.process.send_signal(signal.SIGTERM)
        self.driver.quit()

    def test(self, wait_time_limit, form_xpath):
        WebDriverWait(self.driver, wait_time_limit).until(EC.staleness_of(By.XPATH, form_xpath))