import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# CHROME_DRIVER_PATH = '/Users/khalilj/myGit/WorldOfGames/web_drivers/chromedriver73'
APP_BASE_URL = 'http://server:5000'
SELENIUM_BASE_URL = 'http://selenium-hub:4444/wd/hub'


def test_scores_service(page):
    # driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Remote(
        command_executor=SELENIUM_BASE_URL,
        desired_capabilities=DesiredCapabilities.CHROME
    )

    try:
        driver.get(APP_BASE_URL)
        driver.find_element_by_id("player_name").send_keys("Khalil")
        driver.find_element_by_id("play").submit()

        driver.find_element_by_id("games-1").click()
        driver.find_element_by_id("play").click()

        driver.find_element_by_name("number").send_keys("1")
        driver.find_element_by_id("check_result").submit()

        driver.get(APP_BASE_URL + page)
        elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "score")))
        score = int(elem.text)
        driver.quit()
        return True if 1 <= score <= 1000 else False
    except Exception as ex:
        print(ex.args[0])
        driver.quit()
        return False


def main():
    os.system("/bin/bash ./tests/wait-for-grid.sh")

    result = test_scores_service("/savegame")
    if result:
        return "Test finished successfully"
    return "Test Failed"


if __name__ == '__main__':
    res = main()
    print(res)
