from reportlab.pdfgen import canvas

def criar_pdf_com_texto(texto, pdf_path):
    c = canvas.Canvas(pdf_path)
    largura_pagina, altura_pagina = c._pagesize

    # Adicionar texto ao PDF
    c.drawString(10, altura_pagina - 30, texto)

    c.save()

# Exemplo de uso
texto_exemplo = "Caso: 206321654, Ordem de Serviço: 5412544, data: 21/04/2023"
criar_pdf_com_texto(texto_exemplo, 'documento_teste.pdf')
