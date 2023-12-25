# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    try:
        nome_usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        if nome_usuario != senha:
            break
        else:
            print("Sua senha não pode ser igual ao nome de usuário")
    except ValueError:
        ("Error")

