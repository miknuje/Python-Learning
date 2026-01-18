'''
Escreva um programa que leia um valor em metros
e o exiba convertido em centrimetros e milimetros
'''
metros = float(input('Digite quantos metros correu: '))

centimetros = metros * 100
milimetros = metros * 1000

print('Correste {} centimetros ou {} milimetros que são os {} metros que digitaste.'.format(centimetros, milimetros, metros))
