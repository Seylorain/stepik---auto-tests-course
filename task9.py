from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



link = "http://suninjuly.github.io/file_input.html"
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
try:
    browser = webdriver.Chrome('D:\PoForPrograms\chromedriver\chromedriver.exe')
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk")
    element = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '111.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()