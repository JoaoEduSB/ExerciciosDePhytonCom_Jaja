# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de comparação com processamento pela condição considerando a entrada 

#2) Escreva um algoritmo para ler dois valores do teclado e exibir como resposta a subtração dos valores

print("Vamos exibir uma mensagem dependendo do valor digitado")

valorA = int(input("Digite o primeiro valor: "))

valorB = int(input("Digite o segundo valor: "))

while valorB == valorA:
    print("O valor digitado é igual ao primeiro valor, digite novamente:")
    valorB = int(input("Digite o segundo valor:"))

if valorA < valorB :
    print("\n",valorA, "é maior que", valorB, "\n"
    "\nO primeiro valor é maior que o segundo valor\n")
else :
    print("\n",valorB, "é maior que", valorA, "\n"
    "\nO segundo valor é maior que o primeiro valor\n")
