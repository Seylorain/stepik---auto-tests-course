import time
import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver


link = "http://suninjuly.github.io/get_attribute.html"
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome('D:\PoForPrograms\chromedriver\chromedriver.exe')
    browser.get(link)
    img = browser.find_element_by_css_selector(' img')
    x_element = img.get_attribute("valuex")

    #x = x_element.text
    y = calc(x_element)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    checkbox.click()
    rb = browser.find_element_by_css_selector('[id="robotsRule"]')
    rb.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()