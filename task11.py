from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math



link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
try:
    browser = webdriver.Chrome('D:\PoForPrograms\chromedriver\chromedriver.exe')
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()