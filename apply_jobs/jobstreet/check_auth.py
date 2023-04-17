from selenium import webdriver
from selenium.webdriver.common.by import By
from jobstreet.region_domains import region_domains


def check_auth(driver: webdriver.Firefox, job_region: str) -> bool:
    driver.get("https://jobstreet.com")

    if driver.current_url.startswith("https://jobstreet.com"):
        domain = region_domains.get(job_region.lower())
        driver.get(domain)

    loginElementXPath = "//a[@data-automation='Login']"
    loginElement = driver.find_element(By.XPATH, loginElementXPath)

    return loginElement == None
