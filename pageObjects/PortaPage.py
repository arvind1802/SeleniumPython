from selenium.webdriver.common.by import By

from pageObjects.CustomerPage import AddCustomerPage


class Portapage:

    addcustomer = (By.XPATH, "//*[@class='context-menu-button']")
    searchcust  = (By.XPATH, "//input[@placeholder='Global Filter']")
    selOption = (By.XPATH, "//span[@id='actionOpenIcon0']")
    click_cancel = (By.XPATH, "//div[contains(text(),'Cancel')]")
    edit_cancel = (By.XPATH, "//div[contains(text(),'Edit')]")
    Companyname_update= (By.XPATH, "//input[@name = 'companyNameEdit']")
    confirm_cancellationmsg = (By.XPATH, "//h2[contains(text(),'Confirm Cancelletion?')]")
    cancel_it = (By.XPATH, "//button[contains(text(),'Yes, Cancel it')]")
    successmsg = (By.XPATH, "//div[@class='ui-toast-detail']")
    update_cust = (By.XPATH,"// *[contains(text(), 'Update')]")

    def __init__(self, driver):
        self.driver = driver

    def addcust(self):
        self.driver.find_element(*Portapage.addcustomer).click()
        addcustomerpage = AddCustomerPage(self.driver)
        return addcustomerpage

    def searchCust(self):
        return self.driver.find_element(*Portapage.searchcust)

    def selectOption(self):
        return self.driver.find_element(*Portapage.selOption)

    def cancelOption(self):
        return self.driver.find_element(*Portapage.click_cancel)

    def editOption(self):
        return self.driver.find_element(*Portapage.edit_cancel)

    def companyname_Edit(self):
        return self.driver.find_element(*Portapage.Companyname_update)

    def confimCancelMessage(self):
        return self.driver.find_element(*Portapage.confirm_cancellationmsg)

    def updateCustomer(self):
        return self.driver.find_element(*Portapage.update_cust)

    def cancelIt(self):
        return self.driver.find_element(*Portapage.cancel_it)

    def SuccessMessage(self):
        return self.driver.find_element(*AddCustomerPage.successmsg)

