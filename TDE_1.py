EXEC 1: 

numero = 0
numero = int(input("Informe um número: "))
print('Seu Antecessor é:', numero - 1)
print('Seu sucessor é: ', numero + 1)
--------------------------------------------------------------------------------------------------------------
EXEC 2:

idade = int(input('Informe o ano de seu nascimento: '))
print('Em 2022 você terá: ', 2022-idade)
--------------------------------------------------------------------------------------------------------------
EXEC 3:

salario = float(input('Informe seu salário: '))
salary = salario / 1518
salary_limitado = round(salary,2)
print("\n Você recebe o equivalente a", salary_limitado, "salários minimos")
--------------------------------------------------------------------------------------------------------------
EXEC 4: 

produto = float(input("\n Informe o valor de um produto: "))
parcela = float(input("\n Quantas parcelas (1/2/3): "))
valor_final = float
if parcela == 1:
    valor_final = produto * 0.95
    print("\n O valor de 1x parcela com 5% de desconto é: ", valor_final)
elif parcela == 2:
    valor_final = produto / 2
    print("\n O valor de cada parcela é: ", valor_final)
elif parcela ==3:
    valor_final = produto * 1.05
    valor_final = valor_final/3
    print("\n O valor de 3x parcelas com 5% de juros é de: ", valor_final)

--------------------------------------------------------------------------------------------------------------
EXEC 5: 

distance = float(input("Distância total percorrida em quilômetros: "))
comb = float(input("Informe a quantidade em litros de combustível utilizado no trajeto:  "))
economia = distance/comb
print("O consumo médio do autmóvel é de: ", economia, "km\l")

--------------------------------------------------------------------------------------------------------------
EXEC 6: 

h = float(input("Informe a altura do cilindro: "))
r = float(input("\n Infrome o raio do cilindro: "))
total_lt = int
vlr_lt = 50
metros_cubicos=15
total_tudo = 0
volume = 3.14 * (r*r) * h
total_lt = volume / metros_cubicos
