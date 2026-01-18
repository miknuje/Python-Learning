'''
Crie um algoritmo que leia um número e mostre 
o seu dobro, triplo e raiz quadrada.
'''
import math
import cmath

numero = int(input('Escreve um número: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero**(1/2)
#ou 
raizQuadrada2 = math.sqrt(numero)
#ou para numeros negaticos
raizQuadradaN = cmath.sqrt(-25)

print('O numero {} tem como dobro {} e triplo {} e a raiz quadrada é {}.\n'.format(numero, dobro, triplo, raizQuadrada))
print('Extras {}, {}.'.format(raizQuadrada2, raizQuadradaN))
