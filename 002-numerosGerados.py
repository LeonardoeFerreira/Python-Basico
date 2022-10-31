## "Crie um programa que peça para o usuario e imprima todos os
## números pares de 1 até o número fornecido.

numero=1

max = int(input("Digite um inteiro maior que 1:"))
print("Numero pares entre 1 e ", max, ".")

while numero <=max:
    if numero%2==0:
        print(numero, end="")
    numero+=1


