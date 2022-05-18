from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("ХУЙ")

input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("ХУЙ")

input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("ХУЙ")

input4 = browser.find_element(By.ID, "country")
input4.send_keys("ХУЙ")

button = browser.find_element(By.ID, "submit_button")
button.click()


time.sleep(10)
# çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
browser.quit()
