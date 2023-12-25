# Desenvolva um scanner de portas usando sockets, semelhante ao exercício anterior com Scapy, mas usando bibliotecas de socket para criar conexões.

import socket

def scan_ports(target, ports):
    open_ports = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Define um timeout para a conexão

        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
        
        s.close()

    return open_ports

target = input("Digite o endereço IP ou nome de domínio do alvo: ")
port_range = input("Digite o intervalo de portas (ex: 1-100): ")

start_port, end_port = map(int, port_range.split('-'))
ports = range(start_port, end_port + 1)

open_ports = scan_ports(target, ports)

if open_ports:
    print("Portas abertas:")
    for port in open_ports:
        print(port)
else:
    print("Nenhuma porta aberta encontrada.")