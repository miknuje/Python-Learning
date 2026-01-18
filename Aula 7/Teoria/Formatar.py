nome = input("Qual é seu nome?\n")
print("Prazer em te conhecer {:20}!".format(nome))
print("Prazer em te conhecer {:>20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:=^20}!".format(nome))

#Operadores Aritméticos

n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma é {0}, a multiplicação é {2}, o divisão é {1:.3f}'.format(s, d, m), end='. ')
print('A divisão inteira é {}, a potência é {}, o resto é {}'.format(di, e, r))
