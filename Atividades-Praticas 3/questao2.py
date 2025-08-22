'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''

peso = float(input("Qual é o seu peso em Kilos: "))
altura = float(input("Qual a sua altura em CM: "))
imc = peso / (altura**2)

if peso <= 0 or altura <= 0:
    print("Dados inválidos! O peso e a altura devem ser maiores que zero.")
else:
    print("Dados válidos!")

if imc < 18.5:
  classificacao = "Abaixo do peso"
elif imc < 25:
  classificacao = "Peso Normal"
elif imc < 30:
  classificacao = "Sobrepeso"

else:
  classificacao = "Obeso, vai caminhar criança"

print(f"Seu imc é {imc:.2f} e sua classificação é: {classificacao}")