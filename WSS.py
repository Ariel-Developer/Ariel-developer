from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as py
import time
class WSS_web():
    def __init__(self):
        '''
        Condição Você terá que Escanear o qrcode até 20s ,
        para que o programa funcione 100%
        '''
        self.nome_do_ctt()
        self.Abrir_wpp()
    def nome_do_ctt(self):
        while True:
            self.nome_ctt = input("\033[1;34mQual ctt deseja mandar a msg:")
            self.msg_ctt = input("\033[1;34mMensagem: ")
            print('\033[1;31m-'*50)
            self.confirmar = input("\033[1;31mconfirmar? [S/N]: ").upper()
            if self.confirmar == "S":
                break
            print('\033[1;31m-' * 50)
    def Abrir_wpp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://web.whatsapp.com/")
        self.driver.maximize_window()
        time.sleep(20)
        py.click(138, 285)
        py.write(self.nome_ctt)
        py.press("enter")
        py.write(self.msg_ctt)
        py.press("enter")
go = WSS_web()




































