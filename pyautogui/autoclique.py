import pyautogui
import time


# Defina as coordenadas onde você deseja clicar
x, y = 500, 500

# Loop para realizar cliques repetidos
while True:
    pyautogui.click(x, y)  # Clique na posição especificada
    time.sleep(1)  # Aguarde 1 segundo entre os cliques