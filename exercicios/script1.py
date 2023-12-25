# Crie um script Scapy que envie pacotes ICMP ping para um host específico e imprima as respostas

from scapy.all import IP, ICMP, sr1

def icmp_ping(target_ip, count=4):
    for i in range(count):
        packet = IP(dst=target_ip) / ICMP()
        response = sr1(packet, timeout=2, verbose=False)
        
        if response:
            print(f"Resposta recebida de {response.src}: ICMP Seq={response.getlayer(ICMP).seq}")
            response.show()

if __name__ == "__main__":
    target_ip = "192.168.3.9"  # Substitua pelo endereço IP do host alvo
    num_pings = 4  # Número de pacotes ICMP a serem enviados
    
    print(f"Enviando {num_pings} pings para {target_ip}...")
    icmp_ping(target_ip, num_pings)
