import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
def calc(a, b):
  return str(a+b)

try:
    browser = webdriver.Chrome('D:\PoForPrograms\chromedriver\chromedriver.exe')
    browser.get(link)

    num1 = browser.find_element_by_css_selector('[id="num1"]')
    num2 = browser.find_element_by_css_selector('[id="num2"]')

    x = num1.text
    y = num2.text

    z = calc(int(x), int(y))

    select = Select(browser.find_element_by_css_selector('[id="dropdown"]'))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()