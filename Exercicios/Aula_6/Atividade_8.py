litros = int(input('Digite uma quantidade de litros: '))
combustivel = float(input('Digite o valor do combustivel: '))
valor = litros * combustivel
print(f'O valor do abastecimento é {valor: .2f} reais')