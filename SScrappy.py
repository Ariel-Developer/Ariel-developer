from bs4 import BeautifulSoup
import requests
import mysql.connector
from tqdm import tqdm
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class v1_SS:
    def __init__(self):
        self.email()
        self.verificar_emails()
        self.navegando_site()
        self.coletando_dados_site()
        self.enviando_to_DataBase()
    def email(self):
        self.Email = input("\033[1;92mDigite seu E-mail para receber os conteúdo:\033[0;0m")
    def verificar_emails(self):
         self.check_email = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', self.Email)
         if self.check_email:
            print("\033[1;92mEmail valido\033[0;0m")
         else:
             print("\033[1;91mO E-mail que inseriu está errado\033[1;91m")
    def navegando_site(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(1000, 700)
        self.driver.get("https://lista.mercadolivre.com.br/celulares#D[A:celulares]")
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
        self.driver.close()
    def coletando_dados_site(self):
        for temp in tqdm(range(5), desc="Extraindo.."):
            time.sleep(1)
        self.response = requests.get("https://lista.mercadolivre.com.br/celulares#D[A:celulares]")
        self.site = BeautifulSoup(self.response.text, "html.parser")
        self.divs_celulares = self.site.findAll("div", class_="ui-search-result__content-wrapper shops__result-content-wrapper")
    def enviando_to_DataBase(self):
        try:
            for self.celular in self.divs_celulares:
                self.conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="64350929B",
                    database="sistema_ss"
                )
                self.modelo_celular = self.celular.find("h2", class_="ui-search-item__title shops__item-title").get_text()
                self.modelo_preco_celular = self.celular.find("span", class_="price-tag-fraction").get_text()
                cursor = self.conexao.cursor()
                cursor.execute(f"INSERT INTO celulares (Modelo, Preço) VAlUES ('{self.modelo_celular}',{self.modelo_preco_celular})")

                self.conexao.commit()
                self.conexao.close()
                cursor.close()
            print("\033[1;92mEnviando para Banco de dados com sucesso!")
        except AttributeError:
            print("\033[1;31mO dados não foi coletado ainda!")

mainloop = v1_SS()

