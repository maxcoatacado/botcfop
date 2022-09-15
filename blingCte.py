from ssl import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

navigator = webdriver.Chrome()

navigator.get('https://www.bling.com.br/ctes.php#list')
sleep(5)

email = navigator.find_element(By.CSS_SELECTOR, '#username')
email.send_keys('nieliton@maxcoatacado.com.br')

sleep(5)

senha = navigator.find_element(By.CSS_SELECTOR, '.senha-input')
senha.send_keys('Psfm1234@')
senha.submit()

loginSubmit = navigator.find_element(By.CSS_SELECTOR, '.button-primary-site') 
loginSubmit.click()


# site = BeautifulSoup(navigator.page_source, 'html.parser')

# print(site.prettify())
