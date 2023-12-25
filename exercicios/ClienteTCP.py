import socket

HOST = 'localhost'
PORT = 9002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
mensagem_recebida = data.decode()  # Decodifique os bytes recebidos para obter a mensagem

print("Mensagem recebida do servidor:", mensagem_recebida)

s.close()  # Feche a conexão após receber a mensagem