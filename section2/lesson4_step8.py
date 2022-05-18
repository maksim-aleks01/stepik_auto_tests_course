from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  browser = webdriver.Chrome()
  # говорим WebDriver ждать все элементы в течение 5 секунд
  browser.implicitly_wait(5)

  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  #price_el = browser.find_element_by_id("price")
  
  price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
  )
  button = browser.find_element_by_id("book")
  button.click()

  #Решение капчи
  x_el = browser.find_element_by_id("input_value")
  x = x_el.text

  y = calc(x)

  answer_el = browser.find_element_by_id("answer")
  answer_el.send_keys(y)

  start_btn = browser.find_element_by_id("solve")
  start_btn.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
