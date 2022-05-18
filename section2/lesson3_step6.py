from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    start_btn = browser.find_element_by_css_selector(".trollface")
    start_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_el = browser.find_element_by_id("input_value")
    x = x_el.text

    y = calc(x)

    answer_el = browser.find_element_by_id("answer")
    answer_el.send_keys(y)

    start_btn = browser.find_element_by_css_selector('.btn.btn-primary')
    start_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
