from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)
    
    chbox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    chbox.click()

    radiobtn = browser.find_element_by_xpath("//label[@for='robotsRule']")
    radiobtn.click()
    
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
