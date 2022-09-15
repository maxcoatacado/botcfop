from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
navigator = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
navigator.get('https://www.bling.com.br/ctes.php#list')

email = navigator.find_element(By.CSS_SELECTOR, '#username')
print(email)
# email.send_keys('nieliton@maxcoatacado.com.br')


# sleep(5)

# senha = navigator.find_element(By.CSS_SELECTOR, '.senha-input')
# senha.send_keys('Psfm1234@')
# senha.submit()

# loginSubmit = navigator.find_element(By.CSS_SELECTOR, '.button-primary-site') 
# loginSubmit.click()


# site = BeautifulSoup(navigator.page_source, 'html.parser')

# print(site.prettify())
