import socket

def scan_ports(host, port_range):
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((host, port))
            open_ports.append(port)
            sock.close()
        except (socket.timeout, ConnectionRefusedError):
            pass

    return open_ports

def main():
    host = input("Digite o endereço IP ou nome de host: ")
    start_port = int(input("Digite a porta inicial: "))
    end_port = int(input("Digite a porta final: "))

    port_range = range(start_port, end_port + 1)
    open_ports = scan_ports(host, port_range)

    if open_ports:
        print(f"Portas abertas em {host}:")
        for port in open_ports:
            print(f"Porta {port} está aberta")
    else:
        print(f"Nenhuma porta aberta encontrada em {host}")

if __name__ == "__main__":
    main()