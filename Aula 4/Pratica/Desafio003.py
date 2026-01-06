#Com o que aprendi na aula: daria isto
numero1 = input("Primeiro número é ")
numero2 = input("Segundo número é ")

print('A soma é {}'.format(numero1+numero2))

#Para acertar:
numero1 = int(input("Primeiro número é "))
numero2 = int(input("Segundo número é "))

print('A soma é {}'.format(numero1+numero2))

#Ou assim:

numero1 = int(input("Primeiro número é "))
numero2 = int(input("Segundo número é "))
numero3 = numero1 + numero2

print('A soma entre {0} e {1} é {2}'.format(numero1, numero2, numero3))