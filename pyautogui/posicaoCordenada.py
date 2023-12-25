import pyautogui

# Espere alguns segundos para mover o mouse para a posição desejada
print("Mova o mouse para a posição desejada...")
pyautogui.sleep(5)  # Aguarde 5 segundos para mover o mouse

# Obtenha as coordenadas atuais do cursor do mouse
x, y = pyautogui.position()

# Exiba as coordenadas
print(f"As coordenadas atuais do mouse são: x = {x}, y = {y}")
'''Neste exemplo, você terá alguns segundos para mover o mouse para a posição desejada na tela. Depois disso, o programa irá capturar as coordenadas (x, y) do cursor do mouse e exibi-las na tela.

Você pode usar essas coordenadas no seu programa de robô de autoclique para clicar em locais específicos na tela.

Lembre-se de que as coordenadas podem variar dependendo da resolução e do tamanho da tela do seu computador, portanto, certifique-se de ajustar as coordenadas conforme necessário para o ambiente em que você está trabalhando.
'''




