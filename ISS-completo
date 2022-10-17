from tkinter import *
import re
import pyautogui as py
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import pyttsx3
import smtplib
import email.message
import pandas as pd
from tqdm import tqdm


# programa principal
class SS_d:
    def __init__(self):
        self.intro()
        self.login_email()
        self.verificar_email()
        self.produto()
        self.site_coletando()
        self.Enviar_para_email()
        self.repositorio()
    def intro(self):
        def pular_skip(event):
            self.intro1_Tk.destroy()
        def sound_intro(event):
            engine = pyttsx3.init()
            engine.say("A principal função deste programa"
                       "é coletar dados sobre qualquer produto"
                       "e Fazer uma integração com o banco de dados"
                       "MySQL(SQL), "
                       "    "
                       "sobre o programa"
                       "Ele é simples de usar"
                       "Em menos de 10s ele coleta toda informação do produto e manda para o seu Email!")
            engine.runAndWait()

        self.intro1_Tk = Tk()
        self.intro1_Tk.title("Intro")
        self.intro1_Tk.resizable(False, False)
        self.intro1_Tk.geometry("463x380")
        self.intro1_Tk.iconbitmap("favicon (1).ico")
        bg_intro1_tk = PhotoImage(file="Versão 1.0.png")

        self.background_intro1_tk = Label(self.intro1_Tk, image=bg_intro1_tk)
        self.background_intro1_tk.pack()

        lg = PhotoImage(file="Sound-Check.png")
        self.som_logo = Label(self.intro1_Tk, image=lg, bg="#00C2CB")
        self.som_logo.place(x=90, y=20, height=40, width=50)
        self.som_logo.bind("<Button-1>", sound_intro)

        self.pular_intro = Label(self.intro1_Tk, text="Pular", font="Helveltica 11 bold", bg="#C22323", fg='black',
                                 width=6, height=1)
        self.pular_intro.place(x=375, y=343)
        self.pular_intro.bind("<Button-1>", pular_skip)
        self.intro1_Tk.mainloop()
    def login_email(self):
        self.email_1 = input("\033[1;94mDigite seu E-mail para receber os dados: ")
    def verificar_email(self):
        self.verificando_email = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', self.email_1)
        if self.verificando_email:
            print("\033[1;92mEmail valido!")
            time.sleep(1)
        else:
            print("\033[1;91mEmail invalido")
            self.login_email()
    def produto(self):
        self.ask_produto = input("\033[1;94mQual produtor deseja coletar:\033[m ")
        py.alert(title="Aviso", text="O programa irá começar ,não pressione nenhuma tecla!")
    def site_coletando(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.get(f"https://lista.mercadolivre.com.br/{self.ask_produto}#D[A:{self.ask_produto}]")
        time.sleep(1)
        self.navegador.close()
        self.response = requests.get(f"https://lista.mercadolivre.com.br/{self.ask_produto}#D[A:{self.ask_produto}]")
        self.pagina = BeautifulSoup(self.response.text, "html.parser")
        self.divs = self.pagina.findAll("div", class_="ui-search-result__wrapper shops__result-wrapper")
        self.lista_modelo = []
        self.lista_modelo_preco = []
        for div in self.divs:
            self.modelo_produto = div.find("h2",
                                           class_="ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title")
            self.modelo_produto_price = div.find('span', class_="price-tag-fraction")
            if self.modelo_produto:
                print(self.modelo_produto.get_text() + " ", self.modelo_produto_price.get_text())
                self.lista_modelo.append(self.modelo_produto.get_text())
                self.lista_modelo_preco.append(self.modelo_produto_price.get_text())
            else:
                self.submodelo_produto = div.find("h2", class_="ui-search-item__title shops__item-title")
                self.modelo_produto_price2 = div.find("span", class_="price-tag-fraction")
                self.lista_modelo_preco.append(self.modelo_produto_price2.get_text())
                self.lista_modelo.append(self.submodelo_produto.get_text())
                print(self.submodelo_produto.get_text())

    def Enviar_para_email(self):
        self.tabela = pd.DataFrame(self.lista_modelo, columns={"Item"})
        self.tabela['Preço'] = self.lista_modelo_preco
        corpo_email = f"""
            <h1>Tabelas de produto</h2>
            <p>Aqui está a tabela com os dados coletado</p>
            {self.tabela.to_html()}
          """
        msg = email.message.Message()
        msg["Subject"] = "Tabela"
        msg["From"] = "Arielleo2005@gmail.com"
        msg["To"] = self.email_1
        password = "ynxrhdbeobgfzhxt"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo_email)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()

        s.login(msg["from"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        for i in tqdm(range(3),desc="Enviando.."):
            time.sleep(1)
        print("\033[1;92mEmail enviado")
    def repositorio(self):
        self.git = Tk()
        self.git.title("Repositorio-GitHub")
        self.git.iconbitmap("Github-ICon.ico")
        repositorio_git = PhotoImage(file="MeuRepositorio.jpg")
        self.qrcode_git = Label(self.git, image=repositorio_git).pack()
        self.git.mainloop()


work = SS_d()

