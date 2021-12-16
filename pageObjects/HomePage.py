
from selenium.webdriver.common.by import By

from pageObjects.ServicesPage import ServicesPage


class HomePage:
    myservices = (By.XPATH, "//span[@class='fa detail-icon icon-ICO-Detail-Opportunity icon-lg fa-lg']")

    def __init__(self,driver):
        self.driver = driver


    def getServicesIcon(self):
        self.driver.find_element(*HomePage.myservices).click()
        servicePage = ServicesPage(self.driver)
        return servicePage


