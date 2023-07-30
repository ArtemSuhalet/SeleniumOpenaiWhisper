from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='/Users/mymacbook/PycharmProjects/pythonProject/openai_whisper/firefoxdriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)


url = 'https://drive.google.com/file/d/1mOHre6TCgEin3qEqmSjzKf5OzwsSPIA3/view?usp=drivesdk'# ссылка на видео файл для дальнейшей транскрипции
try:
    driver.get(url)
    input_tab = driver.find_element(By.ID('identifierId'))
    input_tab.send_keys('artem.s@gart.tech')
    input_tab.send_keys(Keys.ENTER)

except Exception as ex:
     print(ex)

