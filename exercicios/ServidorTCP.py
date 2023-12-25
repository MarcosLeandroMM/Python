# Implemente um servidor socket simples que aceita conexões de clientes e envia uma mensagem de boas-vindas. Crie um cliente socket para se conectar ao servidor e receber a mensagem.

import socket

HOST = 'localhost'
PORT = 9002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Aguardando conexão de um cliente")
conn, ender = s.accept()

print("Conectado em", ender)
mensagem = "Seja bem-vindo ao servidor!"
conn.send(mensagem.encode())  # Envie a mensagem após codificar em bytes
conn.close()  # Feche a conexão após enviar a mensagem