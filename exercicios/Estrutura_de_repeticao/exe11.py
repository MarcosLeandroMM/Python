# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Solicita o tamanho do arquivo em MB e a velocidade do link em Mbps
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))

# Converte a velocidade de Mbps para MB por minuto
velocidade_internet_mb_por_minuto = velocidade_internet_mbps / 8 / 60  # 1 byte = 8 bits, 1 minuto = 60 segundos

# Calcula o tempo aproximado de download em minutos
tempo_download_minutos = tamanho_arquivo_mb / velocidade_internet_mb_por_minuto

# Exibe o resultado
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")