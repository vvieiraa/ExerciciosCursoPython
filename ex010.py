#Exercício 10: Converta reais para dólares, considerando US$3.27 = R$1.00

n1 = int(input('Digite quantos Reais você possui: '))

conversor = (n1 / 3.27)

print('Você consegue comprar: US${:.2f} dólares com R${} reais'.format(conversor, n1))
