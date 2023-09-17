import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")
############################################################################################################################################################################################
altura = float(input("Digite sua altura em metros: \n").replace(",", "."))

peso = float(input("Digite seu peso em kg: \n").replace(",", "."))

imc = peso / (altura ** 2)

print("Seu imc é:", imc)

if imc < 18:
    print("Você esta abaixo do peso ideal\n")
if imc >= 18 and imc <= 24.9:
    print("Você esta no peso ideal\n")
if imc >= 25 and imc <= 29.9:
    print("Você esta com sobrepeso\n")
if imc >= 30 and imc < 34.9:
    print("Você esta com Obesidade grau I\n")
if imc >= 35 and imc < 39.9:
    print("Você esta com Obesidade grau II\n")
if imc >= 40:
    print("Você esta com Obesidade grau III\n")

input()