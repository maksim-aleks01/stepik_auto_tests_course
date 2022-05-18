from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name_input = browser.find_element_by_css_selector('[name="firstname"]')
    name_input.send_keys('Zalypa')
    
    name_lstname = browser.find_element_by_css_selector('[name="lastname"]')
    name_lstname.send_keys('Zalypa')
    
    name_email = browser.find_element_by_css_selector('[name="email"]')
    name_email.send_keys('Zalypa')
    
    button = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    button.send_keys(file_path)

    send_btn = browser.find_element_by_css_selector('[type="submit"]')
    send_btn.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
