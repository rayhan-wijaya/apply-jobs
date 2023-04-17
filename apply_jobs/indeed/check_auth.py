from selenium import webdriver
from selenium.webdriver.common.by import By


def check_auth(driver: webdriver.Firefox) -> bool:
    driver.get("https://indeed.com")

    signinElementXPath = "//div[@data-gnav-element-name = 'SignIn']"
    signinElement = driver.find_element(By.XPATH, signinElementXPath)

    return signinElement == None
