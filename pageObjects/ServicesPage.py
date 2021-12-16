
from selenium.webdriver.common.by import By

from pageObjects.PortaPage import Portapage


class ServicesPage:

    servicesicon = (By.CSS_SELECTOR, ".dd-header-left")
    vocieandcommtwo = (By.XPATH, "//*[@class='button-icon icon product-icon icon-ico-conferencing icon-4x icon-lg']")
    voiceandcomm = (By.XPATH, "//strong[contains(text(),'Voice & Communication')]")
    voicec = (By.XPATH, "//strong[contains(text(),'TEST - MIGRATION ACC')]")

    def __init__(self, driver):
        self.driver = driver


    def servicesPagedropdown(self):
        return self.driver.find_element(*ServicesPage.servicesicon)

    def selectaccount(self):
        return self.driver.find_element(*ServicesPage.voicec)


    def voicecommone(self):
        return self.driver.find_element(*ServicesPage.voiceandcomm)


    def voicecommtwo(self):
        self.driver.find_element(*ServicesPage.vocieandcommtwo).click()
        portaPage = Portapage(self.driver)
        return portaPage

