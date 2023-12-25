import speech_recognition as sr
import pyaudio
import time

# Configurar o objeto PyAudio para capturar áudio do microfone
p = pyaudio.PyAudio()
taxa_de_amostragem = 44100  # Taxa de amostragem em Hz
canais = 1  # Mono (1 canal)
amostras_por_frame = 512  # Tamanho do buffer de áudio
formato = pyaudio.paInt16
stream = p.open(format=formato,
                channels=canais,
                rate=taxa_de_amostragem,
                input=True,
                frames_per_buffer=amostras_por_frame)

# Configurar o objeto Recognizer (Reconhecedor) do SpeechRecognition
recognizer = sr.Recognizer()

print("Iniciando reconhecimento de fala em tempo real...")

try:
    while True:
        # Ler áudio do microfone
        audio = stream.read(amostras_por_frame)

        # Reconhecer o áudio usando o Google Web Speech API
        texto_reconhecido = recognizer.recognize_google(audio, language="pt-BR", show_all=False)

        # Imprimir o texto reconhecido
        print("Texto reconhecido:", texto_reconhecido)

        # Adicione uma pausa para evitar o consumo excessivo de recursos da CPU
        time.sleep(0.1)

except KeyboardInterrupt:
    # Encerrar o fluxo de áudio ao pressionar Ctrl+C
    print("Encerrando o programa...")
    stream.stop_stream()
    stream.close()
    p.terminate()
