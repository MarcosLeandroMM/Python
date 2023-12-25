valor = int(input("Digite um número inteiro: "))

match valor:
    case 1 | 2:
        print("O valor é 1 ou 2!")

    case 2:
        print("O valor é 3!")

    case 3:
        print("O valor não é 1, 2 ou 3.")


""" Guarda em Padrões:
Você pode adicionar uma cláusula if a um padrão, conhecida como "guarda". Se a guarda for falsa, a correspondência continua para tentar o próximo bloco de caso.
Exemplo: """


match valor:
    case valor if valor % 2 == 0:
        print("O número é par.")
    case valor:
        print("O valor é ímpar.")

""" Padrões de Sequência e Desempacotamento:
Os padrões de sequência têm suporte ao desempacotamento, semelhante ao desempacotamento de atribuições. Você pode usar [x, y, *rest] e (x, y, *rest) para desempacotar sequências.
Exemplo: """
