import unittest
import os, time
from app.models import User, Chat, ChatQuestion, ChatResponse
from app import initapp, db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER = os.path.join(os.getcwd(), "chromedriver.exe")

class systemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        service = Service(DRIVER)
        self.driver = webdriver.Chrome(service=service)

        if not self.driver:
            self.skipTest("Web browser not available")
        else:
            app = initapp("config.TestingConfig")
            app_context = app.app_context()
            app_context.push()
            db.create_all()
            self.driver.maximize_window()
            self.driver.get("http://localhost:5000/")

    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.remove()
            db.drop_all()
    
    def test_register(self):
        self.driver.find_element("id", "start-button").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login/")

        self.driver.find_element("id", "back-button").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/")

        self.driver.find_element("id", "start-button").click()
        self.driver.find_element("id", "register-link").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/register/")

        valid_first_name = valid_last_name = "Test"
        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        valid_confirm_password = "Test1234$"
        register = self.driver.find_element("id", "register-button")

        self.driver.find_element("id", "firstname").send_keys("")
        self.driver.find_element("id", "lastname").send_keys("")
        self.driver.find_element("id", "email").send_keys("")
        self.driver.find_element("id", "newpw").send_keys("")
        self.driver.find_element("id", "confirmPW").send_keys("")
        register.click()


        warnings = self.driver.find_element(By.ID, "firstname").get_attribute("validationMessage")

        # self.assertEqual(warnings[0], "Please fill out this field.")

        # self.driver.find_element("id", "first-name").send_keys(valid_first_name)
        # self.driver.find_element("id", "last-name").send_keys(valid_last_name)
        # self.driver.find_element("id", "email").send_keys(valid_email)
        # self.driver.find_element("id", "password").send_keys(valid_password)
        # self.driver.find_element("id", "confirm-password").send_keys(valid_confirm_password)
        # self.driver.find_element("id", "register-button").click()


if __name__ == "__main__":
    unittest.main(verbosity=2)