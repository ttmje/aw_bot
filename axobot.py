import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def launch():
    driver = webdriver.Chrome()
    url = driver.command_executor._url
    session_id = driver.session_id
    driver = webdriver.Remote(command_executor=url, desired_capabilities={})
    driver.close()
    driver.session_id = session_id
    driver.get("https://axo2moon.com/?r=394231")
    try:
        elem = driver.find_element_by_class_name("showcase__btn btn btn-orange claim-btn ng-binding")
        elem.click()
    except NoSuchElementException:
        pass
    return driver
while True:
    launch()
