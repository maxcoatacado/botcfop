from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
navigator = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
navigator.get('https://www.bling.com.br/ctes.php#list')
sleep(5)


email = navigator.find_element(By.CSS_SELECTOR, '#username')
email.send_keys('nieliton@maxcoatacado.com.br')
print(email)


# sleep(5)

# senha = navigator.find_element(By.CSS_SELECTOR, '.senha-input')
# senha.send_keys('Psfm1234@')
# senha.submit()

# loginSubmit = navigator.find_element(By.CSS_SELECTOR, '.button-primary-site') 
# loginSubmit.click()


# site = BeautifulSoup(navigator.page_source, 'html.parser')

# print(site.prettify())
