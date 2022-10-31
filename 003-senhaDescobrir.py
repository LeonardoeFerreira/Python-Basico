senha="1234"

tentativa=input("Digite a senha:")

while(senha!=tentativa):
    print("Senha errada! Tente novamente!")
    tentativa=input("Digite a senha: ")

print("Senha correta. Entrando no sistema... ")