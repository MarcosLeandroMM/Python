x = 1
s = []
j = ''
i = ''
k = ''
t = ''
n = ''

x not in s # False caso um item de s for igual caso contrário True

s[i:j] # i-ésimo item de s, origem 0

s[i:j:k] # fatia de s de i até j com passo k
len(s) # comprimento de s
min(s) # menor item de s
max(s) # maior item de s

s.count(x) # numero total de ocorrência de x em s

'''
Os valores de n menos 0 são tratados como 0 (o que produz uma sequência vazia do mesmo tipo que s). Observe que os itens na sequência s não são copiados; eles são referenciados várias vezes. Isso frequentemente assombra novos programadores Python; considere então que:

'''

lists = [[]] * 3
lists[0].append(3)

'''O que aconteceu é que [[]] é uma lista de um elemento contendo uma lista vazia, então todos os três elementos de [[]] * 3 são referências a esta única lista vazia. Modificar qualquer um dos elementos de lists modifica a lista vazia. Podemos criar uma lista de listas diferentes dessa maneira:

'''
lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)

'''
As operações na tabela a seguir são definidas em tipos sequência mutáveis. A ABC collections.abc.MutableSequence é fornecida para tornar mais fácil a implementação correta dessas operações em tipos sequências personalizados.

Na tabela s é uma instância de um tipo de sequência mutável, t é qualquer objeto iterável e x é um objeto arbitrário que atende a qualquer restrição de tipo e valor imposto por s (por exemplo bytearray só aceita inteiros que atendam a restrição de valor 0 <= x <= 255).
'''
s[i] = x # item i de s é substituído por x
s[i:j] = t # fatias de s de i até j são substituídas pelo conteúdo do iterável t

del s[i:j] # o mesmo que s[i:j] = []

s.append(x) # adiciona x no final da sequência (mesmo que s[len(s):len(s)] = [x])

s.clear() # remove todos os itens de s (mesmo que del s[:])

s.copy() # cria um cópia rasa de s (mesmo que s[:])

s.extend(t) # estende s como conteúdo de t

s *= n # atualiza s como conteúdo por n vezes

s.insert(i, x) # insere x dentro de s no índice dado por i (igual a s[i:i] = [x])

s.pop(i) # retorna o item em i e também o remove de s

s.remove(x) # remove o primeiro item de s sendo s[i] igual a x

s.reverse() # inverte os itens de s in-place

