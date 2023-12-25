# Escreva um programa que implemente uma comunicação cliente-servidor usando sockets UDP, onde o cliente envia uma mensagem e o servidor responde com uma confirmação.

import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print("Aguardando mensagem do cliente...")
data, ender = s.recvfrom(1024)
mensagem_recebida = data.decode()
print("Mensagem recebida do cliente:", mensagem_recebida)

confirmação = "Confirmado"
s.sendto(confirmação.encode(), ender)