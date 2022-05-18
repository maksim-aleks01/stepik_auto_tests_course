from selenium import webdriver
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  from selenium import webdriver
  browser = webdriver.Chrome()
  browser.implicitly_wait(5)
  browser.get("http://suninjuly.github.io/cats.html")

  math = browser.find_element_by_id("button")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
