from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import sqlite3
import pandas as pd
import smtplib
import email.message

class raspagem:
    def __init__(self):
        self.login_email()
        self.raspagem_de_dados()
        self.enviando_dados_to_Database()
        self.enviando_to_email()
    def login_email(self):
        self.email_usuario = input(
            '\033[1;92mdigite o seu email para receber o conteúdo:'
        )
    def raspagem_de_dados(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://lista.mercadolivre.com.br/celular#D[A:celular]")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]").click()
        self.driver.close()
        # Pegar ID,Span,Class
        self.url = 'https://lista.mercadolivre.com.br/celular#D[A:celular]'
        self.response = requests.get(self.url)
        self.site = BeautifulSoup(self.response.text, "html.parser")
        self.celular = self.site.findAll("li", class_="ui-search-layout__item shops__layout-item")
        for i in tqdm(range(2)):
            time.sleep(1)
    def enviando_dados_to_Database(self):
        for self.celulares in self.celular:
            self.marca = self.celulares.find("h2", class_="ui-search-item__title shops__item-title").get_text().strip()
            self.preco = self.celulares.find("span", class_="price-tag-amount").get_text().strip()
            self.Data = sqlite3.connect("WebAuto.db")
            self.cursor = self.Data.cursor()
            self.cursor.execute("INSERT INTO celulares VALUES(:Marca, :preco)", (self.marca, self.preco))
            self.cursor.execute("SELECT * FROM celulares")
            self.cadastro = self.cursor.fetchall()
            self.tabela = pd.DataFrame(self.cadastro, columns={"Marca", "Preco"})
            self.Data.commit()
            self.Data.close()
        print(self.tabela)
    def enviando_to_email(self):
        corpo_email = f"""
           <p>Olá {self.email_usuario}</p>
           <p>Tabela dos celulares</p>
           <p>Planilha {self.tabela.to_html()}</p>
           """
        msg = email.message.Message()
        msg["Subject"] = "Dados coletados"
        msg["From"] = "arielleo2005@gmail.com"
        msg["To"] = "arielleo2005@gmail.com"
        password = "zcfqerlqwptircbn"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo_email)
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["from"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        print("\033[1;92mEmail enviado com sucesso!!")

rp = raspagem()
