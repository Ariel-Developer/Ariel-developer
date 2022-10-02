#importações
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
#Entrando No G1
driver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver)
driver.get('https://g1.globo.com/g1-em-1-minuto/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="cookie-banner-lgpd"]/div/div[2]/button').click()

#Coletando títulos de noticias
time.sleep(4)
driver.close()
for i in tqdm(range(5), desc="Extraindo"):
    time.sleep(1)
response = requests.get("https://g1.globo.com/g1-em-1-minuto/")
site = BeautifulSoup(response.text, 'html.parser')
noticias = site.find_all("div", class_="feed-post-body")
for noticia in noticias:
    titulo = noticia.find('div', class_='_evt').get_text()
    print(titulo)










