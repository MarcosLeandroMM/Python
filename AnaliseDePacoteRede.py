
import pcapy
import dpkt

def packet_handler(header, data):
    try:
        eth = dpkt.ethernet.Ethernet(data)

        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            src_ip = ".".join(map(str, map(int, ip.src)))
            dst_ip = ".".join(map(str, map(int, ip.dst)))

            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                print(f"Protocolo: TCP, Origem: {src_ip}:{tcp.sport}, Destino: {dst_ip}:{tcp.dport}")

            elif isinstance(ip.data, dpkt.udp.UDP):
                udp = ip.data
                print(f"Protocolo: UDP, Origem: {src_ip}:{udp.sport}, Destino: {dst_ip}:{udp.dport}")

            else:
                print(f"Protocolo: {ip.data.__class__.__name__}, Origem: {src_ip}, Destino: {dst_ip}")

    except Exception as e:
        print(f"Erro ao analisar pacote: {e}")

if __name__ == "__main__":
    interface = "eth0"  # Substitua pelo nome da sua interface de rede

    # Abre a interface de rede para captura
    cap = pcapy.open_live(interface, 65536, True, 100)

    print(f"Iniciando a captura na interface {interface}...")

    # Começa a captura de pacotes
    cap.loop(-1, packet_handler)