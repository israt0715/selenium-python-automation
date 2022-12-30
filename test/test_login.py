from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_loginsuccess():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
