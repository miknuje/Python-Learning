'''
Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço, com 5% de desconto.
'''

preco = float(input('Preço do produto: '))

desconto = preco * 0.05
precoComDesconto = preco - desconto

print('O preço {:.2f} com o desconto de 5% é {:.2f}.'.format(preco, precoComDesconto))
