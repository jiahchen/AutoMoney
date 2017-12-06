from selenium import webdriver
from page_object.FreeBitCoHomePage import FreeBitCoHomePage
from config import CONFIG

def main():
    #driver = webdriver.PhantomJS(executable_path='/home/dev/test/phantomjs')
    driver = webdriver.Firefox()
    home = FreeBitCoHomePage(driver)
    home.navigate()
    home.click_login_toggle()
    home.input_email_address(CONFIG['email'])
    home.input_password(CONFIG['passwd'])
    home.click_login_button()

if __name__ == '__main__':
    main()