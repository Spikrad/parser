from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import datetime

options = webdriver.ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Spikrad\\AppData\\Roaming\\JetBrains\\PyCharmCE2023.1\\light-edit\\chromedriver.exe",
    options=options
)

try:
    driver.maximize_window()
    driver.get("https://www.tutu.ru/")
    time.sleep(5)

    # Ввод города отправления в поле
    departure_city = driver.find_element(By.XPATH,
                                         "/html/body/div[3]/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/input")
    departure_city.clear()
    departure_city.send_keys("Махачкала")
    time.sleep(1)
    departure_city.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    departure_city.send_keys(Keys.ENTER)

    # Ввод города назначения в поле
    arrival_city = driver.find_element(By.XPATH,
                                       "/html/body/div[3]/div[1]/div[5]/div/div[1]/div/div[2]/div[3]/div[1]/input")
    arrival_city.send_keys("Сочи")
    time.sleep(1)
    arrival_city.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    arrival_city.send_keys(Keys.ENTER)

    # Поле даты отправления
    date_of_dispatch = driver.find_element(By.XPATH,
                                           "/html/body/div[3]/div[1]/div[5]/div/div[1]/div/div[2]/div[4]/div[1]/input")
    today = datetime.date(2023, 10, 12)
    date_of_dispatch.send_keys("{}.{}.{}".format(today.day, today.month, today.year))
    date_of_dispatch.send_keys(Keys.ENTER)
    time.sleep(1)

    # Поле даты возвращения
    return_date = driver.find_element(By.XPATH,
                                      "/html/body/div[3]/div[1]/div[5]/div/div[1]/div/div[2]/div[6]/div[1]/input")
    today = datetime.date(2023, 11, 12)
    return_date.send_keys("{}.{}.{}".format(today.day, today.month, today.year))
    return_date.send_keys(Keys.ENTER)

    # Клик на кнопку
    print('click')

    time.sleep(5)
    a = driver.find_element(By.CLASS_NAME, '_1uSe5b5VpATGBsj5MOqkJy').text
    print(a)
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
