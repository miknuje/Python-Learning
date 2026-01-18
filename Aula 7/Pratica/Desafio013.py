'''
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento
'''

salario = float(input('Salário atual: '))

aumento = salario * 0.15
salarioComAumento = salario + aumento

print('O salario {:.2f} com o aumento de 15% é {:.2f}.'.format(salario, salarioComAumento))
