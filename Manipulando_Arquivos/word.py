from docx import Document

def encontrar_palavras_chave(doc_path, palavras_chave):
    document = Document(doc_path)
    palavras_encontradas = []

    for paragraph in document.paragraphs:
        for palavra in palavras_chave:
            if palavra.lower() in paragraph.text.lower():
                palavras_encontradas.append(palavra)
    
    return palavras_encontradas

palavras_chave = ["Python", "Excel", "PDF"]
palavras_encontradas = encontrar_palavras_chave('document.docx')


