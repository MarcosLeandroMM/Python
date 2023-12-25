'''

Funções Aninhadas:
Defina uma função externa que cria uma função interna. A função interna deve aceitar dois argumentos e realizar alguma operação com eles. Em seguida, a função externa retorna a função interna. Use a função externa para criar funções internas personalizadas.

'''

def criar_funcao_interna(operacao):
    # Função interna que realiza uma operação com dois argumentos
    def funcao_interna(a, b):
        if operacao == "soma":
            return a + b
        elif operacao == "subtracao":
            return a - b
        elif operacao == "multiplicacao":
            return a * b
        elif operacao == "divisao":
            if b == 0:
                return "Erro: divisão por zero"
            return a / b
        else:
            return "Operação inválida"

    # Retorna a função interna
    return funcao_interna

# Criar funções internas personalizadas
soma = criar_funcao_interna("soma")
subtracao = criar_funcao_interna("subtracao")
multiplicacao = criar_funcao_interna("multiplicacao")
divisao = criar_funcao_interna("divisao")

# Exemplo de uso das funções internas
resultado_soma = soma(5, 3)
resultado_subtracao = subtracao(8, 2)
resultado_multiplicacao = multiplicacao(4, 6)
resultado_divisao = divisao(10, 2)

print("Soma:", resultado_soma)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
