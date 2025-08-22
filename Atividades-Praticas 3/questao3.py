'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Primeiro, converte a temperatura para Celsius


if origem == "C":
    celsius = temperatura
elif origem == "F":
    celsius = (temperatura - 32) * 5/9
elif origem == "K":
    celsius = temperatura - 273.15
else:
    print("Dados Inválidos")

# Depois, converte de Celsius para a unidade desejada
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9/5) + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Dados inválidos")

print(f"\nOrigem  {temperatura:.2f}°{origem} = Destino  {resultado:.2f}°{destino}")

