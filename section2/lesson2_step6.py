from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
       
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)
    
    chkox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    chkox.click()
    
    radiobtn = browser.find_element_by_xpath("//label[@for='robotsRule']")

    #Scroll in to view
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()
    
    button = browser.find_element_by_tag_name("button")
    button.click()
        
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
