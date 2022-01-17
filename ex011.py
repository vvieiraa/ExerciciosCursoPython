#Exercício 11: Calcule a área de uma parede e quantos litros de tinta são necessários para pintar (considere que a tinta possua o rendimento de 1L=2m²)

altura = int(input('Qual a altura da parede (m): '))
largura = int(input('Qual a largura da parede (m): '))
tinta = int(input('Quantos litros de tinta você possui: '))

area = altura * largura
rendimento = tinta * 2

print('A parede possui {}m² de área. E com {}L de tinta você consegue pintar {}m².'.format(area, tinta, rendimento))


