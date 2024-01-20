from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


class Udemy:
    def __init__(self, course_url):
        """paste your course url."""
        self.__url = course_url

        self.__driver = webdriver.Chrome(chrome_option)
        self.__driver.get(self.__url)

        WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div  button.ud-heading-sm'))
        )

        time.sleep(5)
        expand_all = self.__driver.find_element(By.CSS_SELECTOR, '.curriculum--curriculum-sub-header--m_N_0 button.ud-btn-medium')
        time.sleep(2)
        # expand_all.click()
        self.__driver.execute_script("arguments[0].click();", expand_all)
        self.__course_contain()

    def __course_contain(self):

        self.__content_detail = []
        all_containers = self.__driver.find_elements(By.CLASS_NAME, 'accordion-panel-module--panel--3_kkG.section--panel--1zoAn')

        for single_container in all_containers:
            heading = single_container.find_element(By.CLASS_NAME, 'section--section-title--wcp90')
            day = heading.text.split("-")[0].strip()
            day_heading = heading.text.split('-')[-1]
            titles = single_container.find_elements(By.CSS_SELECTOR, '.ud-unstyled-list.ud-block-list li div.section--row--3sLRB span')

            title_name = [title.text for title in titles]

            self.__content_detail.append({day: {"main_heading": day_heading, "all_title": title_name}})

            # time.sleep(10)
            # self.__driver.quit()

    def get_details(self):
        """return json data"""
        return self.__content_detail
