from selenium import webdriver
from selenium.webdriver.common.by import By


def check_auth(driver: webdriver.Firefox) -> bool:
    driver.get("https://indeed.com")

    signupElementXPath = "//div[@data-gnav-element-name = 'SignIn']"
    signupElement = driver.find_element(By.XPATH, signupElementXPath)

    driver.close()

    return signupElement == None
