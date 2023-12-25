# criando servidor para testar comunicação com o cliente

import socket

def send_image(client_socket, image_path):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            client_socket.sendall(image_data)
    except Exception as e:
        print(f"Erro ao enviar a imagem: {e}")
        
        


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8001)
    
try:
    server_socket.bind(server_address)
    server_socket.listen()
    
    print("Aguardando conexão do cliente...")
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")
    
      # Enviando a imagem para o cliente
    image_path = 'Captura.png' # caminho da imagem
    send_image(client_socket, image_path)
      
except Exception as e:
    print(f"Erro: {e}")
finally:
    client_socket.close()
    client_socket.close()
    
    
