
print("Calculo para verificacao do IMC")
nome = input("Por favor digite o seu nome: ")
print("Seja bem vindo(a) {} ".format(nome))
h = float(input("Insira a sua altura em centimetros separada por ponto: "))
peso = float(input("Digite o seu peso: "))
imc = peso / h ** 2
print("o seu imc é {:.2f}".format(imc))
if imc < float(16.00):
    print("Baixo peso Grau III")
if imc >= float(16.00) and imc <= float(16.99):
    print("Baixo peso Grau II")
if imc >= float(17.00) and imc <= float(18.49):
    print("Baixo peso Grau I")
if imc >= float(18.50) and imc <= float(24.99):
    print("Peso ideal")
if imc >= float(25.00) and imc <= float(29.99):
    print("Sobrepeso")
if imc >= float(30.00) and imc <= float(34.99):
    print("Obesidade Grau I")
if imc >= float(35.00) and imc <= float(39.99):
    print("Obesidade Grau II")
if imc >= float(40.0 ):
    print("Obesidade Grau III")