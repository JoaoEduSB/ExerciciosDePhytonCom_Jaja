# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício que trás o maior valor

#3) Escreva um algoritmo para ler dois valores do teclado e exibir como resposta a multiplicação dos valores.

print("Vamos exibir o maior valores entre os 3 digitados")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if ((a > b) & (a > c)):
    print("O maior valor é A, que vale ", a)
elif ((b > a) & (b > c)):
    print("O maior valor é B, que vale ", b)
else:
    print("O maior valor é C, que vale", c)
