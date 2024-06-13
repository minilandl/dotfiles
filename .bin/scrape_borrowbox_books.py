#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

# User Info
LIBRARY_LOCATION = 'cockburn'
LIBRARY_CARD_NUMBER = 'cl119m2464004d'
PASSCODE = '1234'

# Constants
LOGIN_URL = f"https://{LIBRARY_LOCATION}.borrowbox.com/login"
MY_LOANS_URL = f"https://{LIBRARY_LOCATION}.borrowbox.com/home/my-loans"
DOWNLOAD_BUTTON_CLASS = 'button-download'
PROGRESS_BUTTON_CLASS = 'download-button'
USERNAME_FIELD_ID = 'form-input-1'
PASSWORD_FIELD_ID = 'form-input-2'
LOGIN_BUTTON_XPATH = '//button[@type="submit" and contains(@class, "signin-button")]'
COOKIE_FILE = "cookies.pkl"
WAIT_TIME = 5
DOWNLOAD_WAIT_TIME = 60


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("detach", True)
    webdriver_service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=webdriver_service, options=chrome_options)

def login(driver, username, password):
    driver.get(LOGIN_URL)
    username_field = driver.find_element(By.ID, USERNAME_FIELD_ID)
    password_field = driver.find_element(By.ID, PASSWORD_FIELD_ID)
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH)
    login_button.click()
    time.sleep(WAIT_TIME)

def save_cookies(driver):
    pickle.dump(driver.get_cookies(), open(COOKIE_FILE, "wb"))

def load_cookies(driver):
    cookies = pickle.load(open(COOKIE_FILE, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def navigate_to_my_loans(driver):
    driver.get(MY_LOANS_URL)
    time.sleep(WAIT_TIME)

def download_books(driver):
    download_buttons = driver.find_elements(By.CLASS_NAME, DOWNLOAD_BUTTON_CLASS)
    for i in range(len(download_buttons)):
        driver.get(MY_LOANS_URL)
        time.sleep(WAIT_TIME)
        download_buttons = driver.find_elements(By.CLASS_NAME, DOWNLOAD_BUTTON_CLASS)
        download_buttons[i].click()
        time.sleep(WAIT_TIME)
        progress_button = driver.find_element(By.CLASS_NAME, PROGRESS_BUTTON_CLASS)
        progress_button.click()
        time.sleep(DOWNLOAD_WAIT_TIME)

def main():
    driver = setup_driver()
    login(driver, LIBRARY_CARD_NUMBER, PASSCODE)
    save_cookies(driver)
    load_cookies(driver)
    navigate_to_my_loans(driver)
    download_books(driver)
    driver.quit()

if __name__ == "__main__":
    main()
