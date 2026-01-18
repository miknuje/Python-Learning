'''
Faça um programa que leia um número inteiro e
mostre na tela o seu número sucessor e seu antecessor
'''

numero = int(input('Escreva um número: '))

antecessor = numero - 1
sucessor = numero + 1

print ('O sucessor do numero {}, é {}, enquanto o antecessor é {}'.format(numero, sucessor, antecessor))
