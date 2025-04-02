EXEC 1:
numero = int(input("Informe um número: "))
if numero % 2 == 0:
    print("Número é par")
elif print("Número é ímpar"):
    print(Fim)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 2:
idade = int(input('Informe o ano de seu nascimento: '))
maior = 2023-idade
print('Em 2023 você terá: ', maior)
if maior>=18:
    print("Você já é de maior, pode fazer sua CNH")
elif print("Você é de menor ainda "):
    print(fim)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 3: 
import math
numero = int(input("Informe um número: "))
numero = math.isqrt(numero)
if numero<0:
    print("Número inválido")
elif print("A raíz quadrada do número informado é: ", numero):
 print(fim)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 4:
diametro = int(input("Informe o diâmetro da abóbora: "))
if 15 <= diametro < 20:
    print("Abóbora dentro dos padrões médios")
elif print("Abóbora fora dos padrões médios"):
    print(fim)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 5: 
num_foto = int(input("Informe a quantidade de fotocópias: "))
if num_foto<=100:
    print("O Valor é: ", num_foto*0.25)
elif num_foto>100: print("O valor das fotocópias são: ", num_foto*0.20, "reais")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 6: 
h = float(input("Informe sua altura em m: "))
sexo = int(input("Informe seu sexo: \n 1 - masculino \n 2 - feminino \n "))
if sexo == 1:
    peso_ideal = (72.7 * h) - 58
    print("Peso ideal: {:.2f} kg".format(peso_ideal))
elif sexo == 2:
    peso_ideal = (62.1 * h) - 44.7
    print("Peso ideal: {:.2f} kg".format(peso_ideal))
else:
    print("Sexo inválido! Por favor, insira 1 para masculino ou 2 para feminino.")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 7: 
massa = int(input("Informe sua massa(kg): "))
altura = float(input("Informe sua altura(m): "))
imc = 0

imc = massa / (altura*altura)

if 18.5 <= imc < 25:
    print("IMC NORMAL ")
elif imc<18.5:
    print("IMC abaixo do normal")
else:
    print("IMC acima do normal")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 8: 
minuto = int(input("Informe a quantidade de minutos no estacionamento: "))

final = 0
if minuto<=60:
    print("Valor mínimo, R$ 8,00")
else:
    minuto_add = minuto - 60
    valor_add = (minuto_add / 15) * 1.50
    valor_total = 8 + valor_add
    print("Valor fracionado R$: ", valor_total)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 9: 
idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não votante")
elif 18 <= idade <= 65:
    print("Eleitor Obrigatório")
elif idade >= 16 or idade > 65:
    print("Eleitor Facultativo")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 10: 
massa = int(input("Informe sua massa(kg): "))
altura = float(input("Informe sua altura(m): "))
imc = 0

imc = massa / (altura*altura)

if imc<18.5:
    print("Abaixo do peso ")
elif 18.5<imc<25:
    print("Peso normal")
elif 25<imc<30:
    print("Acima do peso")
elif imc>30:
    print("Obeso")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 11: 
idade = int(input("Informe sua idade: "))

if 5<= idade <=7:
    print("\n Infantil A")
elif 8<= idade <=10:
    print("\n Infantil B")
elif 11<= idade <=13:
    print("\n Juvenil A")
elif 14<= idade <=17:
    print("\n Juvenil B")
elif idade>18:
    print("\n Adulto")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 12: 
peso = int(input("Informe seu peso em KG: "))
lbs = peso * 2.20

if lbs>=201:
    print("\n Peso-pesado")
elif 176<= lbs <=200:
    print("\n Cruzador")
elif 169 <= lbs <= 175:
    print("\n Meio-pesado")
elif 161<= lbs <= 168:
    print("\n Super médio")
elif lbs<161:
    print("\n Categoria inferior a super médio")
------------------------------------------------------------------------------------------------------------------------------------
EXEC 13: 
produto = float(input("\n Informe o valor de um produto: "))
parcela = float(input("\n 1x \n 2x \n 3x \n 4x \n Quantas parcelas:  "))
valor_final = float
parte = float
if parcela == 1 :
    valor_final = produto * 0.92
    print("\n O valor em 1x com 8% de desconto é: ", valor_final)
elif parcela == 2 :
    valor_final = produto * 0.96
    parte = valor_final / 2
    print("\n O valor de cada parcela é: ", parte , "R$ \n O valor final do produto com 4% de desconto é: ", valor_final)
elif parcela == 3 :
    parte = valor_final/3
    print("\n O valor de 3x parcelas: ", parte)
elif parcela == 4:
    valor_final = produto * 1.04
    parte = valor_final/4
    print("\n O valor de cada parcela é: ", parte , "R$ \n O valor final do produto com 4% de acréscimo: ", valor_final)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 14: 
num1 = int(input("Digite o primeiro número : "))
num2 = int(input("Digite o segundo número : "))
num3 = int(input("Digite o terceiro número : "))
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f"O maior número é: ", maior)
------------------------------------------------------------------------------------------------------------------------------------
EXEC 15: 
num1 = int(input("Digite o primeiro número : "))
num2 = int(input("Digite o segundo número : "))
num3 = int(input("Digite o terceiro número : "))

if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2
print(f"Os números em ordem decrescente são: ", num1,",", num2,",", num3)

