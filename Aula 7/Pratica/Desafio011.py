'''
Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade de 
tinta necessária para pintá-la, sabendo que cada litro 
de tinta pinta uma área de 2m².
'''
largura = float(input('Escreva a largura: '))
altura = float(input('Escreva a altura: '))

area = largura * altura

tinta = area / 2

print('A quantidade de tinta é {:.2f}L.'.format(tinta))