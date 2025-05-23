cadastro_login = input("Crie seu Login: ")
cadastro_senha = input("Crie uma senha: ")
usuario = input("Digite seu login")
senha = input("Digite sua senha")

while cadastro_login != usuario or cadastro_senha != senha:
    print("Usuario invalido, tente novamente")
    usuario = input("Digite seu login")
    senha = input("Digite sua senha")
print("usuario valido")