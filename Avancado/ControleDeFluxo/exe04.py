'''
Anagramas:
Escreva uma função que receba uma palavra e retorne todos os anagramas possíveis. Por exemplo, para a palavra "abc", os anagramas seriam "abc", "acb", "bac", "bca", "cab" e "cba"

'''

def generate_anagrams(word):
    if len(word) <= 1:
        return [word]
    
    # Caso base: Se a palavra tem apenas uma letra, retorne uma lista com ela mesma.

    anagrams = []

    for i in range(len(word)):
        first_char = word[i]
        remaining_chars = word[:i] + word[i+1:]
        
        # Gere anagramas recursivamente para o restante das letras.
        for sub_anagram in generate_anagrams(remaining_chars):
            anagrams.append(first_char + sub_anagram)

    return anagrams

# Exemplo de uso:
palavra = "abc"
anagramas = generate_anagrams(palavra)
print(anagramas)
