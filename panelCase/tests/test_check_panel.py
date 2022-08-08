from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.campaigns_page import CampaignsPage
from pages.design_page import DesignPage
from pages.home_page import HomePage
from pages.goals_page import GoalsPage
from pages.launch_page import LaunchPage
from pages.login_page import LoginPage
from pages.rules_page import RulesPage
from pages.segment_page import SegmentPage


class TestCheckPanel():
    """The section where we make the settings and create the objects"""

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://seleniumautomation.inone.useinsider.com/"
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    campaigns_page = CampaignsPage(driver)
    rules_page = RulesPage(driver)
    segment_page = SegmentPage(driver)
    design_page = DesignPage(driver)
    goals_page = GoalsPage(driver)
    launch_page = LaunchPage(driver)

    def navigate_to_home_page(self):
        """driver settings made and website published"""

        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)


if __name__ == '__main__':
    TestCheckPanel()
