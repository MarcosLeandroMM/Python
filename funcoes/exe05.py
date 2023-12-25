'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas
'''

def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto
    custo_com_imposto = custo + imposto
    return custo_com_imposto

# Exemplo de uso da função
taxa = 0.1  # 10% de imposto
custo_item = 100  # Custo do item antes do imposto
novo_custo = somaImposto(taxa, custo_item)

print(f"O novo custo com imposto é: R$ {novo_custo:.2f}")