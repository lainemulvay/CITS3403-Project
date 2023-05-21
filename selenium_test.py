import unittest
import os, time
from werkzeug.security import generate_password_hash
from app.models import User, Chat, ChatQuestion, ChatResponse
from app import initapp, db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
            self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            self.driver.close()
    
    def test_register(self):
        self.driver.get("http://localhost:5000/")
        time.sleep(1)
        self.driver.find_element("id", "start-button").click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login/")

        self.driver.find_element("id", "back-button").click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/")

        self.driver.find_element("id", "start-button").click()
        time.sleep(1)
        self.driver.find_element("id", "register-link").click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/register/")

        valid_first_name = valid_last_name = "Test"
        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        register = self.driver.find_element("id", "register-button")

        register.click()
        time.sleep(1)
        warning1 = self.driver.find_element(By.ID, "firstname").get_attribute("validationMessage")

        # chrome on windows show "Please fill out this field"
        self.assertEqual(warning1, "Please fill in this field.")

        self.driver.find_element("id", "firstname").send_keys(valid_first_name)
        self.driver.find_element("id", "lastname").send_keys(valid_last_name)
        self.driver.find_element("id", "email").send_keys("123")
        register.click()

        warning1 = self.driver.find_element(By.ID, "email").get_attribute("validationMessage")
        self.assertEqual(warning1, "Please include an '@' in the email address. '123' is missing an '@'.")

        self.driver.find_element("id", "email").clear()
        self.driver.find_element("id", "email").send_keys(valid_email)
        self.driver.find_element("id", "newpw").send_keys("123")
        register.click()

        warning1 = self.driver.find_element(By.ID, "newpw").get_attribute("validationMessage")
        register.click()

        # chrome on windows show "Please match the requested format."
        self.assertEqual(warning1, "Please match the format requested.")

        self.driver.find_element("id", "newpw").clear()
        self.driver.find_element("id", "newpw").send_keys(valid_password)
        self.driver.find_element("id", "confirmpw").send_keys("Test1234")
        register.click()
  
        warning1 = self.driver.find_element(By.ID, "confirmpw").get_attribute("validationMessage")
        self.assertEqual(warning1, "Passwords don't match.")

        self.driver.find_element("id", "confirmpw").clear()
        self.driver.find_element("id", "confirmpw").send_keys(valid_password)
        register.click()

        time.sleep(1)
        prompt = self.driver.find_element("id", "swal2-title").text
        self.assertEqual(prompt, "Email already exists")

    def test_login(self):
        self.driver.get("http://localhost:5000/")
        time.sleep(1)
        self.driver.find_element("id", "start-button").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login/")

        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        login = self.driver.find_element("id", "signin-button")

        login.click()
        warning1 = self.driver.find_element("id", "email").get_attribute("validationMessage")
        self.assertEqual(warning1, "Please fill in this field.")

        self.driver.find_element("id", "email").send_keys(valid_email)
        login.click()
        warning1 = self.driver.find_element("id", "password").get_attribute("validationMessage")
        self.assertEqual(warning1, "Please fill in this field.")

        self.driver.find_element("id", "password").send_keys("123")
        login.click()
        time.sleep(1)
        warning1 = self.driver.find_element("id", "swal2-html-container").text
        self.assertEqual(warning1, "Invalid password")

        self.driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

        self.driver.find_element("id", "password").clear()
        self.driver.find_element("id", "password").send_keys(valid_password)
        login.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/chat/")
    
    def test_chat(self):
        self.driver.get("http://localhost:5000/login/")
        time.sleep(1)
        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        self.driver.find_element("id", "email").send_keys(valid_email)
        self.driver.find_element("id", "password").send_keys(valid_password)
        self.driver.find_element("id", "signin-button").click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/chat/")

        welcome_message = "Let's get started!"

        input = "Hello"
        send = self.driver.find_element("id", "submit-chat-input")
        
        self.driver.find_element("id", "chat-input-message").send_keys(input)
        send.click()

        time.sleep(5)
        responses = self.driver.find_elements(By.CLASS_NAME, "message-content")

        self.assertIn(welcome_message, responses[0].text)
        # Can't test response as it is random
        self.assertNotEqual(responses[2].text, "")

    def test_history(self):
        self.driver.get("http://localhost:5000/login/")
        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        self.driver.find_element("id", "email").send_keys(valid_email)
        self.driver.find_element("id", "password").send_keys(valid_password)
        self.driver.find_element("id", "signin-button").click()
        time.sleep(1)

        self.driver.get("http://localhost:5000/history/")
        self.assertEqual(self.driver.current_url, "http://localhost:5000/history/")

        chat_number = self.driver.find_element("id", "chat-number").text
        self.assertEqual(chat_number, "Chat number: 1")

        self.driver.find_element("id", "view-chat-btn").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/history/1")

        time.sleep(1)
        welcome_message = "Let's get started!"
        responses = self.driver.find_elements(By.CLASS_NAME, "message-content")
        self.assertIn(welcome_message, responses[0].text)
        self.assertEqual(responses[1].text, "Hello")
        self.assertEqual(responses[2].text, "Hello! How may I assist you today?")

        self.driver.find_element(By.CLASS_NAME, "backbtn").click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/history/")
    
    def test_profile_and_log_out(self):
        self.driver.get("http://localhost:5000/login/")
        valid_email = "Test@email.com"
        valid_password = "Test1234$"
        self.driver.find_element("id", "email").send_keys(valid_email)
        self.driver.find_element("id", "password").send_keys(valid_password)
        self.driver.find_element("id", "signin-button").click()
        time.sleep(1)

        self.driver.get("http://localhost:5000/profile/")
        self.assertEqual(self.driver.current_url, "http://localhost:5000/profile/")

        time.sleep(1)
        first_name = self.driver.find_element("id", "firstname").get_attribute("value")
        last_name = self.driver.find_element("id", "lastname").get_attribute("value")
        email = self.driver.find_element("id", "email").get_attribute("value")
        self.assertEqual(first_name, "Test")
        self.assertEqual(last_name, "Test")
        self.assertEqual(email, "test@email.com")

        self.driver.find_element("id", "update").click()

        self.driver.find_element("id", "firstname").clear()
        self.driver.find_element("id", "firstname").send_keys("Change")
        self.driver.find_element("id", "lastname").clear()
        self.driver.find_element("id", "lastname").send_keys("Change")
        self.driver.find_element("id", "email").clear()
        self.driver.find_element("id", "email").send_keys("Change@email.com")

        self.driver.find_element("id", "save").click()
        time.sleep(1)

        prompt = self.driver.find_element("id", "swal2-title").text
        self.assertEqual(prompt, "Account updated")
        self.driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

        self.driver.find_element("id", "password-page").click()
        time.sleep(1)
        
        self.driver.find_element("id", "oldpw").send_keys(valid_password)
        self.driver.find_element("id", "newpw").send_keys("Change1234$")
        self.driver.find_element("id", "confirmpw").send_keys("Change1234$")
        self.driver.find_element("id", "update-password").click()

        time.sleep(1)
        prompt = self.driver.find_element("id", "swal2-title").text
        self.assertEqual(prompt, "Password updated")
        self.driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

        first_name = self.driver.find_element("id", "firstname").get_attribute("value")
        last_name = self.driver.find_element("id", "lastname").get_attribute("value")
        email = self.driver.find_element("id", "email").get_attribute("value")
        self.assertEqual(first_name, "Change")
        self.assertEqual(last_name, "Change")
        self.assertEqual(email, "change@email.com")

        self.driver.get("http://localhost:5000/logout/")
        new_email = "Change@email.com"
        new_password = "Change1234$"
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login/")

        self.driver.find_element("id", "email").send_keys(new_email)
        self.driver.find_element("id", "password").send_keys(new_password)
        self.driver.find_element("id", "signin-button").click()
        time.sleep(1)

        self.assertEqual(self.driver.current_url, "http://localhost:5000/chat/")

        self.driver.get("http://localhost:5000/profile/")
        self.driver.find_element("id", "update").click()
        self.driver.find_element("id", "firstname").clear()
        self.driver.find_element("id", "firstname").send_keys("Test")
        self.driver.find_element("id", "lastname").clear()
        self.driver.find_element("id", "lastname").send_keys("Test")
        self.driver.find_element("id", "email").clear()
        self.driver.find_element("id", "email").send_keys(valid_email)
        self.driver.find_element("id", "save").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

        self.driver.find_element("id", "password-page").click()
        time.sleep(1)
        self.driver.find_element("id", "oldpw").send_keys("Change1234$")
        self.driver.find_element("id", "newpw").send_keys(valid_password)
        self.driver.find_element("id", "confirmpw").send_keys(valid_password)
        self.driver.find_element("id", "update-password").click()

if __name__ == "__main__":
    unittest.main(verbosity=2)