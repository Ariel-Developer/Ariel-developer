import requests
import pyttsx3
from bs4 import BeautifulSoup


class cotacao:
    def __init__(self):
        self.ouro()
        self.main()

    def main(self):
        response = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL")
        response = response.json()
        dolar = response['USDBRL']['bid']
        engine = pyttsx3.init()
        engine.say(f"O dólar está : {dolar} Reais.")
        engine.say(f'E o ouro está: {self.valor} Reais.')
        engine.runAndWait()
        print(f"O dolar está : ${dolar}")
        print(f"E o valor do ouro está: R$ {self.valor}")
    def ouro(self):
        response = requests.get("https://goldrate.com/pt-br/grama-do-ouro-preco-cotacao-valor/")
        site = BeautifulSoup(response.text, "html.parser")

        self.valor = site.find('em', class_="price-value").get_text()





go = cotacao()

