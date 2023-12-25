from scapy.all import *

def is_suspicious_packet(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 2:
        return True
    elif packet.haslayer(UDP) and packet[UDP].dport == 53:
        return True
    else:
        return False


def analyze_pcap(file_path):
    suspicious_packets = []
    try:
        packets = rdpcap(file_path)
        for packet in packets:
            if is_suspicious_packet(packet):
                suspicious_packets.append(packet)

    except Exception as e:
        print(f"Erro ao analisar o arquivo {file_path}: {e}")

    return suspicious_packets


if __name__ == "__main__":
    pcap_file = "/home/marcos/wireshark files/CapturePackets.pcapng"
    suspicious_packets = analyze_pcap(pcap_file)

    print(f"Total de pacotes suspeitos encontrados: {len(suspicious_packets)}")
    for i, packet in enumerate(suspicious_packets, start=1):
        print(f"Pacote suspeito {i}:")
        print(packet.summary())