from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

el = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
el.click()

input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("ХУЙ")

input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("ХУЙ")

input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("ХУЙ")

input4 = browser.find_element(By.ID, "country")
input4.send_keys("ХУЙ")

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
button.click()

time.sleep(1)
# çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
browser.quit()

