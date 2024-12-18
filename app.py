import pyautogui
from time import sleep
import pyperclip
import webbrowser
import keyboard

def mover_janela_direita():
    pyautogui.keyDown('win')
    sleep(1)
    pyautogui.keyDown('right')
    sleep(1)
    pyautogui.keyUp('right')
    sleep(1)
    pyautogui.keyUp('win')   
    

# # 1 Abrir a página https://guitarflash.com
webbrowser.open_new_tab('https://guitarflash.com')
sleep(2)
mover_janela_direita()

# 2  Clicar em jogar
sleep(2)
botao_curtir = (pyautogui.locateCenterOnScreen('proj2aula17/botao_curtir.png'))
sleep(2)
pyautogui.moveTo(botao_curtir[0],botao_curtir[1],duration=2)
pyautogui.move(0,62,duration=1)
pyautogui.click()

# 3 Escolher a música e clicar na música

sleep(2)
pyautogui.hotkey('ctrl','f')
sleep(1)
pyautogui.typewrite('Falling In Reverse')
sleep(2)
pyautogui.click(1277,770,duration=3)
sleep(3)

# 4 Rolar 400 pixels para baixo e apertar uma tecla para começar
pyautogui.click(1040,285,duration=1)
pyautogui.scroll(-400)
sleep(4)
pyautogui.hotkey('0')


# 5 Se verificar quando será necessário apertar os botões a,s,j,k,l
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1313,879,(255,255,255)):
        pyautogui.press('a')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(1430,839,(255,255,255)):
        pyautogui.press('s')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(1540,841,(255,255,255)):
        pyautogui.press('d')
        sleep(0.01)