from BasePage import BasePage

class FreeBitCoHomePage(BasePage):
    url = 'https://freebitco.in'
    def click_login_toggle(self):
        self.wait_element_located(10, '//li[@class="login_menu_button"]')
        self.click_element('//li[@class="login_menu_button"]')

    def input_email_address(self, email_address):
        self.fill_form('//input[@id="login_form_btc_address"]', email_address)

    def input_password(self, my_password):
        self.fill_form('//input[@id="login_form_password"]' ,my_password)

    def click_login_button(self):
        self.click_element('//button[@id="login_button"]')

