import math
import locale
####imports
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")
####Variaveis
numero = float(input("Digite um numero\n").replace(",", "."))
numero2 = float(input("Digite o outro numero\n").replace(",", "."))
####Calculos
soma = numero + numero2
subtração = numero - numero2
multiplicação = numero * numero2
divisão = numero / numero2
raiz1 = math.sqrt(numero)
raiz2 = math.sqrt(numero2)
#####prints
print("Soma:\n", soma)
print('Subtração:\n', subtração)
print("Multiplicação:\n", multiplicação)
print("Divisão:\n", divisão)
print("Raiz do primeiro numero:\n", raiz1)
print("Raiz do segundo numero:\n", raiz2)
