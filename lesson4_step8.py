from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:

    # функция для подсчета формулы
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # проверять каждые 10 сек, что элемент появился 
    WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    # найти и нажать на book
    button = browser.find_element(By.ID, "book")
    button.click()

    # выбор числа из значения атрибута
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # ввод результата в поле 
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
     
    # Отправить форму
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла