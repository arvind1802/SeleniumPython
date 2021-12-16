import re
from pathlib import Path

import allure
import pytest
import os

from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from actions.Actions import Actions
from pageObjects.LoginPage import LoginPage
from utilities.Base import Base

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path=Base.ROOT_PATH + "/resources/chromedriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=Base.ROOT_PATH + "/resources/geckodriver")
    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path=Base.ROOT_PATH + "/resources/IEDriverServer.exe")

    driver.get("https://clientzone-stage.platform.is/") # get the url from conf file
    actions = Actions(driver)
    lp = LoginPage(driver)
    actions.sendKeys(lp.getUsername(), "justin.sirunwa@nihilent.com")
    actions.click(lp.clickNextBtn())
    actions.sendKeys(lp.getPassword(), "CUX@QA2021")
    actions.click(lp.clickNextBtn())

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            tc_name = report.nodeid.split("::")[-1]
            #tc_name = re.sub(r'\[.*\]', '', tc_name)
            file_name = Base.ROOT_PATH+"/reports/screenshots/"+tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
