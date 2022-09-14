preco = float(input())
valor_percentual = float(input())
preco_com_aumento = preco + valor_percentual
preco_com_desconto = preco - valor_percentual
print(f'{preco_com_aumento: .2f}')
print(f'{preco_com_desconto: .2f}')
