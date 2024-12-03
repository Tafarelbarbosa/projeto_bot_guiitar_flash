import pyautogui
from time import sleep
import pyperclip
import webbrowser

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
# 3 Escolher a música 
# 4 Clicar na música
# 5 Apertar uma tecla para começar
# 6 Se verificar quando será necessário apertar os botões a,s,j,k,l