from selenium.webdriver.common.by import By


class AddCustomerPage:

    companyname = (By.XPATH, "//input[@placeholder='Company Name']")
    creditlimit = (By.XPATH, "//input[@name='creditLimit']")
    contractname = (By. XPATH, "//input[@placeholder='Contact Name']")
    contactnumber = (By.XPATH, "//input[@placeholder='Contact Number:(27)']")
    contactemail = (By.XPATH, "//input[@placeholder='Contact Email']")
    submit = (By.XPATH, "//button[contains(text(),' Submit ')]")
    successmsg = (By.XPATH, "//div[@class='ui-toast-detail']")

    def __init__(self, driver):
        self.driver = driver

    def getCompanyName(self):
        return self.driver.find_element(*AddCustomerPage.companyname)

    def getCreditlimit(self):
        return self.driver.find_element(*AddCustomerPage.creditlimit)

    def getContactName(self):
        return self.driver.find_element(*AddCustomerPage.contractname)

    def getContactNumber(self):
        return self.driver.find_element(*AddCustomerPage.contactnumber)

    def getContactEmail(self):
        return self.driver.find_element(*AddCustomerPage.contactemail)

    def Submit(self):
        return self.driver.find_element(*AddCustomerPage.submit)

    def SuccessMessage(self):
        return self.driver.find_element(*AddCustomerPage.successmsg)

