import time
import ctypes
import pyautogui

def weblocal():
    url = "https://drive.google.com/drive/u/0/my-drive"
    ctypes.windll.user32.MessageBoxW(0, "O programa requer que o documento escolhido esteja\n"
                                        "no canto superior da direita", "Aviso", 1)
    ctypes.windll.user32.MessageBoxW(0, "Não pressione nenhuma tecla", "programa", 1)
    pyautogui.hotkey("Win", "m")
    pyautogui.hotkey("Win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
    pyautogui.press("enter")
    pyautogui.moveTo(1311, 31)
    pyautogui.mouseDown()
    pyautogui.moveTo(740, 617)
    pyautogui.mouseUp()




weblocal()