import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Data import Data

class Test_AddCustomer(Base):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""Verifying the add customer Scenario.""")
    @allure.story('epic_1')
    @allure.title("Adding New Customer into the Porta")
    @allure.step
    def test_addcust(self, getData):
        wait = WebDriverWait(self.driver, 50)
        log = self.getLogger()
        actions = Actions(self.driver)
        homePage = HomePage(self.driver)
        #time.sleep(50)
        wait.until(EC.visibility_of_element_located(homePage.myservices))
        servicePage = homePage.getServicesIcon()
        time.sleep(20)
        actions.click(servicePage.servicesPagedropdown())
        log.info("Clicked on Service Page DropDown")
        actions.click(servicePage.selectaccount())
        log.info("Selected Account")
        time.sleep(20)
        actions.click(servicePage.voicecommone())
        log.info("Clicked on VoiceCommunication")
        time.sleep(20)
        portaPage = servicePage.voicecommtwo()
        log.info("Clicked on VoiceCommunication 2")
        time.sleep(30)
        addcustomerpage = portaPage.addcust()
        log.info("Clicked on Add Customer button")
        actions.sendKeys(addcustomerpage.getCompanyName(), getData["Company Name"])
        log.info("Entered Company Name")
        actions.sendKeys(addcustomerpage.getCreditlimit(), getData["Credit Limit"])
        log.info("Entered Credit Limit")
        actions.sendKeys(addcustomerpage.getContactName(), getData["Contact Name"])
        log.info("Entered Contact Name")
        actions.sendKeys(addcustomerpage.getContactNumber(), getData["Contact Number"])
        log.info("Entered Contact Number")
        actions.sendKeys(addcustomerpage.getContactEmail(), getData["Contact Email"])
        log.info("Entered Contact Email")
        addcustomerpage.Submit().click()
        time.sleep(2)
        tostermessage = addcustomerpage.SuccessMessage().text
        print(tostermessage)
        assert ("Customer is added successful." in tostermessage)
        log.info("Clicked Submit")

    @pytest.fixture(params=Data.getTestData("addCustomer"))
    def getData(self, request):
        return request.param


