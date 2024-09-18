# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
n = int(input("fatorial de: "))
resultado=1
for i in range(1, n +1):
    resultado *=i
print("o fatorial de" , n, "é" , resultado)
    



