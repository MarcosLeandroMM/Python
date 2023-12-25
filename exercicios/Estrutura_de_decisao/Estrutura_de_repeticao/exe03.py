'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd


'''


while True:
    try:
        nome = input("Digite seu nome: ")
        qtd_caractere_nome = len(nome)
        idade = int(input("Digite sua idade: "))
        salario = float(input("Digite seu salário: "))
        sexo = input("Sexo (f para feminino ou m para masculino): ")
        estado_civil = input("Estado civil (s para solteiro, c para casado, v para viúvo, d para divorciado): ")

        if qtd_caractere_nome > 3 and 0 <= idade <= 150 and salario > 0 and (sexo == 'f' or sexo == 'm') and (estado_civil in ['s', 'c', 'v', 'd']):
            break
        else:
            print("Alguma informação é inválida. Por favor, verifique os critérios.")
    except ValueError:
        print("Valores inválidos. Certifique-se de que a idade seja um número inteiro e o salário um número real.")