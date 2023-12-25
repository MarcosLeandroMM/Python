'''
Gerador de Primos:
Escreva uma função geradora que retorne números primos infinitamente. Use o Crivo de Eratóstenes para implementar a geração de números primos
'''

def prime_sieve():
    primes = []
    yield 2  # 2 é o primeiro número primo
    candidate = 3  # Começamos com o próximo candidato a primo
    while True:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2  # Apenas números ímpares podem ser primos, então pulamos os pares

# Exemplo de uso:
gen = prime_sieve()
for _ in range(10):  # Gere os primeiros 10 números primos
    print(next(gen))


'''
Nesta implementação, a função prime_sieve é um gerador que utiliza o Crivo de Eratóstenes para gerar números primos infinitamente. Ela começa com o número 2, que é o primeiro número primo, e depois itera pelos números ímpares (3, 5, 7, 9, etc.). A cada iteração, verifica se o número é primo ou não, adicionando-o à lista primes se for. Em seguida, incrementa o candidato para o próximo número ímpar. Isso gera números primos infinitamente à medida que você chama next(gen).

Observe que a função prime_sieve pode ser usada para gerar quantos números primos você desejar, simplesmente ajustando o limite da iteração no loop for.

'''

'''A palavra-chave yield em Python é usada em funções para criar geradores. Um gerador é um tipo especial de função que permite pausar sua execução e depois retomá-la de onde parou. Isso é útil para iterar sobre uma sequência de valores, especialmente quando você tem uma sequência potencialmente infinita, como a geração de números primos ou leitura de grandes arquivos de dados.

Quando você usa yield em uma função, a função se torna um gerador. A cada vez que a função com yield é chamada, ela retorna um valor e pausa sua execução. Na próxima chamada, a função retoma sua execução a partir do ponto em que parou na chamada anterior, mantendo seu estado interno.

Aqui está um exemplo simples de uma função geradora:'''


def contador():
    for i in range(5):
        yield i

gen = contador()

for num in gen:
    print(num)

'''Neste exemplo, a função contador é um gerador que produz números de 0 a 4. Quando você itera sobre gen, a função é chamada a cada iteração e pausa sua execução após a linha yield, retornando o valor atual de i. Na próxima iteração, a função retoma a execução do loop for a partir do ponto onde parou, continuando a contar.

O uso de yield é muito útil para economizar memória, pois os valores não precisam ser armazenados em uma lista ou em memória, e também para lidar com sequências potencialmente infinitas de dados de forma eficiente.'''
