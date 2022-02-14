from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://wp/')
time.sleep(5)
print(driver.title)

driver.close()
driver.quit()