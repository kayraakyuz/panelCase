from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    """Performs transactions on the Login Page"""

    EMAIL = (By.ID, "email")
    email = "kayra.akyuz@useinsider.com"
    PASSWORD = (By.ID, "password")
    password = "Besiktas1903!"
    LOGIN_BUTTON = (By.ID, "login-button")

    def writing_email(self):
        """writes email"""
        self.send_text(self.email, *self.EMAIL)

    def writing_password(self):
        """writes password"""
        self.send_text(self.password, *self.PASSWORD)

    def clicking_login_button(self):
        """clicks login button"""
        self.click_element(*self.LOGIN_BUTTON)
