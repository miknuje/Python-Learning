'''
Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dolares pode comprar/trocar.
Euro para dolar.
'''

euros = float(input('Quantos euros tens na carteira? '))

dolares = euros * 1.16

print('Podes ter {} dolares'.format(dolares))
