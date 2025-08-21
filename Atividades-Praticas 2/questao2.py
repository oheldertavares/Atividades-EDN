'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''

nome_do_produto = 'Camiseta'
preco = 50
porcentagem_de_desconto = 20

valor_desconto = preco * (porcentagem_de_desconto/100)
preco_final = preco - valor_desconto

print("Nome do produto: ", nome_do_produto)
print("Preço Original: R$", preco)
print("Valor do desconto: ", porcentagem_de_desconto)
print("Preço final: R$", round(preco_final,2))