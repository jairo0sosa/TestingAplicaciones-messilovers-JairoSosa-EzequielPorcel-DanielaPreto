from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# opcione
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\danie\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)



# Inicializar chrome
driver.get('https://magento.softwaretestingboard.com/')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')))\
    .click()
#email valido
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[2]/div/input')))\
    .send_keys('messicampeon')
#contra valida
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[3]/div/input')))\
    .send_keys('pechofriostodos')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span')))\
    .click()

#esto sierra el navegador que se habre para hacer la prueva
driver.quit()