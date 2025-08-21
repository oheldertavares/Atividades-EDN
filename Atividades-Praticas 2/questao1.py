valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_reais // taxa_dolar
valor_em_euro = valor_em_reais // taxa_euro

print(f"Valor em reais: R$ {valor_em_reais}")
print(f"Valor em Dolar: U$ {valor_em_dolar}")
print(f"Valor em Euro: € {valor_em_euro}")