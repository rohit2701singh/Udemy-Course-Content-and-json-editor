from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class JsonEditor:
    def __init__(self, text_input):
        URL = "https://jsonviewer.stack.hu/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(chrome_options)
        self.__driver.get(url=URL)
        self.__textarea = self.__driver.find_element(By.TAG_NAME, "textarea")
        self.__textarea.send_keys(f"{text_input}")

        self.__format = self.__driver.find_element(By.ID, "ext-gen61")
        self.__format.click()

        # try:
        #     element = WebDriverWait(self.__driver, 2).until(
        #         EC.presence_of_element_located((By.ID, "ext-gen61"))
        #     )
        # except:
        #     self.__driver.quit()

        # self.__driver.implicitly_wait(5)

        time.sleep(5)
        try:
            self.__viewer = self.__driver.find_element(By.CLASS_NAME, "x-tab-strip-text ")
            self.__viewer.click()
        except:
            print("can't show.")
            self.__driver.quit()
