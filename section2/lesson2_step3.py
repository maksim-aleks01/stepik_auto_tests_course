from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element_by_id("num1")
    num1 = num1_element.text

    num2_element = browser.find_element_by_id("num2")
    num2 = num2_element.text

    summ = int(num1) + int(num2)

    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ)) # ищем элемент с текстом "Python"
    
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
