#Exercício 13: Faça uma calculadora de aumento de salário

salario = int(input('Digite o valor do seu salário: '))
aumento = int(input('Digite o % de aumento: '))

novoSalario = ((aumento/100)+1) * salario

print('Esse é o seu novo salário R${:.2f} (com {}% de aumento)'.format(novoSalario, aumento))


