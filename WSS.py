import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.get("https://www.amazon.com.br/Livros/b?ie=UTF8&node=6740748011")
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys("Slipknot")
time.sleep(19)

































