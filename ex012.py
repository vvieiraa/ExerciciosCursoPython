#Exercício 12: Faça uma calculadora de descontos

produto = int(input('Digite o valor do produto: '))
desconto = int(input('Digite o % de desconto: '))

produtoComDesconto = produto * (((desconto/100)-1)*-1)

print('Esse é o novo valor do produto: R${:.2f} (com {}% de desconto)'.format(produtoComDesconto, desconto))
