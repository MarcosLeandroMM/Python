
import socket

HOST = 'localhost'
PORT = 8001

def receive_file(client_socket, file_path):
    try:
        with open(file_path, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"Arquivo recebido e salvo como '{file_path}'.")
    except Exception as e:
        print(f"Erro ao receber o arquivo: {e}")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    file_path = 'Captura1.png'  # Caminho e nome do arquivo a ser recebido
    receive_file(client_socket, file_path)

    client_socket.close()

if __name__ == "__main__":
    main()

            