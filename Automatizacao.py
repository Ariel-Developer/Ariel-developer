import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pyautogui
def vagalume_letra():
    url = "https://www.google.com/search?q=stone+temple+pilots&sxsrf=ALiCzsbmvLED8MlYrx8sV3o9TUIk4MPRmg%3A1659544620524&ei=LKTqYq2_H9351sQPwKG_mA8&ved=0ahUKEwitheG8jav5AhXdvJUCHcDQD_MQ4dUDCA4&uact=5&oq=stone+temple+pilots&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCgguELEDEIMBEEMyBAguEEMyBQguEIAEMgQILhBDMgUILhCABDIECC4QQzIECC4QQzIECC4QQzIECC4QQzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToMCC4QyAMQsAMQQxgCOg8ILhDUAhDIAxCwAxBDGAI6CgguEMcBENEDEEM6BAgAEEM6CwguEIAEELEDEIMBOgsIABCABBCxAxCDAToICC4QgAQQsQM6BAguECc6BQgAEIAEOgsILhCABBDHARCvAToICAAQgAQQsQM6BwguELEDEAo6BwgAEIAEEAo6BwguEIAEEAo6BwgAELEDEAo6CggAELEDEIMBEAo6CgguEIAEENQCEAo6DgguEIAEELEDEIMBENQCOgoILhDHARCvARAKOgQIABAKOgQILhAKOhEILhCABBCxAxCDARDHARDRAzoRCC4QgAQQsQMQgwEQxwEQrwE6DQguEEMQiwMQmAMQqAM6BwguEEMQiwM6DggAEIAEELEDEIMBEIsDOg0ILhBDEIsDEKgDEJgDSgQIQRgASgQIRhgBUOcEWMw7YME8aAdwAXgAgAH7AYgB8xeSAQYwLjIxLjKYAQCgAQHIARO4AQLAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="rso"]/div[4]/div/div[1]/div/a/h3').click()
    driver.find_element(By.XPATH, '//*[@id="topMusicList"]/li[1]/div/div/a').click()
    pyautogui.moveTo(1356, 187)
    pyautogui.mouseDown()
    pyautogui.moveTo(1356, 376)
    pyautogui.click(1356, 376)
    pyautogui.mouseUp()
    driver.minimize_window()
    response = requests.get("https://www.vagalume.com.br/stone-temple-pilots/plush.html")
    vaga = BeautifulSoup(response.text, 'html.parser')
    letra = vaga.find('div', id='lyrics').get_text()
    titulo1 = vaga.find('div', class_='col1-2-1')
    titulo2 = titulo1.find('h1')
    print(titulo2.get_text())
    print(vaga.pre)
    print(f"\n{letra}")



    time.sleep(212324)
vagalume_letra()
