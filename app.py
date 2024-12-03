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
    
'''def mover_janela_cima():
    pyautogui.keyDown('win')
    sleep(1)
    pyautogui.keyDown('up')
    sleep(1)
    pyautogui.keyUp('up')
    sleep(1)
    pyautogui.keyDown('up')
    sleep(1)
    pyautogui.keyUp('up')
    sleep(1)
    pyautogui.keyUp('win')'''

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
pyautogui.typewrite('psycho killer')
musica = (pyautogui.locateCenterOnScreen('proj2aula17/musica.png'))
sleep(2)
pyautogui.click(musica[0],musica[1],duration=2)
sleep(1)

# 6 Rolar 400 pixels para baixo e apertar uma tecla para começar
# 7 Se verificar quando será necessário apertar os botões a,s,j,k,l