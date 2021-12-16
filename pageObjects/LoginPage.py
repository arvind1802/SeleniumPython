from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@name='username']")
    clickNext = (By.XPATH, "//*[@class='icon icon-goto icon-2x']")
    password = (By.XPATH, "//input[@name='password']")
    afterLoginMessage = (By.XPATH,"/html/body/app-root/app-main-layout/div/div/app-supernav-layout/div/div[2]/div/div[1]/h1")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickNextBtn(self):
        return self.driver.find_element(*LoginPage.clickNext)

    def MessageAfterLogin(self):
        return self.driver.find_element(*LoginPage.afterLoginMessage)