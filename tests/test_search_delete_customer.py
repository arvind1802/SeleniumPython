import time

import pytest

from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Data import Data


class Test_deletecustomer(Base):

    def test_deletecustomer(self,getData):
        log = self.getLogger()
        actions = Actions(self.driver)
        homePage = HomePage(self.driver)
        time.sleep(30)
        servicePage = homePage.getServicesIcon()
        time.sleep(3)
        actions.click(servicePage.servicesPagedropdown())
        log.info("Clicked on Service Page DropDown")
        actions.click(servicePage.selectaccount())
        log.info("Selected Account")
        time.sleep(20)
        actions.click(servicePage.voicecommone())
        log.info("Clicked on VoiceCommunication")
        time.sleep(50)
        portaPage = servicePage.voicecommtwo()
        log.info("Clicked on VoiceCommunication 2")
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.info("Scrolled to bottom of page")
        time.sleep(5)
        actions.sendKeys(portaPage.searchCust(), getData["Company Name"])
        log.info("Searched customer Name")
        time.sleep(5)
        actions.click(portaPage.selectOption())
        log.info("Clicked three dots")
        time.sleep(5)
        actions.click(portaPage.cancelOption())
        log.info("Clicked cancel option")
        time.sleep(5)
        actions.click(portaPage.confimCancelMessage())
        log.info("Clicked Confirm option")
        actions.click(portaPage.cancelIt())
        time.sleep(2)
        tostermessage = portaPage.SuccessMessage().text
        assert ("Customer is cancelled successful." in tostermessage)
        log.info("Clicked Cancel It option")
        log.info( "New Canceled Added Successfully")


    @pytest.fixture(params=Data.getTestData("searchAndDeleteCustomer"))
    def getData(self, request):
        return request.param