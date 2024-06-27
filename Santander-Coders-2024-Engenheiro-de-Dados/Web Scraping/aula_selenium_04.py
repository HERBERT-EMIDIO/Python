#pip install selenium = navegador que simula 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://site.com')
driver.quit()