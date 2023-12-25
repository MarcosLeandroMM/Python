import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = "Olá, estou conectado ao servidor!"
s.sendto(mensagem.encode(), (HOST, PORT))

data, _ = s.recvfrom(1024)
mensagem_recebida = data.decode()
print("Mensagem recebida do servidor:", mensagem_recebida)