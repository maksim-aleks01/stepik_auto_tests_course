import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")

driver.execute_script("alert('Robots at work');")


time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
