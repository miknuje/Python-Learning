'''
Faça um programa que leia um número inteiro qualquer
e mostre na tela a sua tabuada.
'''
n1 = int(input('Digite o seu número: '))

for i in range(11):
    r = n1 * i
    print('{} Vezes {} = {}'.format(n1, i, r))

#Ou como ainda não tem loops em nenhuma das aulas

n1 = int(input('Digite o seu número: '))

print(n1*0)
print(n1*1)
print(n1*2)
print(n1*3)
print(n1*4)
print(n1*5)
print(n1*6)
print(n1*7)
print(n1*8)
print(n1*9)
print(n1*10)

#Mas como podem ver não é eficiente e é demorado para escrever
