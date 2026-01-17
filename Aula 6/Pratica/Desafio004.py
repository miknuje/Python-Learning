resposta = input('Digite algo: ')

print(type(resposta))
if resposta.isnumeric() == True:
    print('{}, é um número! \n '.format(resposta))
else:
    print('{}, não é um número! \n '.format(resposta))
if resposta.isalpha():
    if resposta.isupper() == True:
        print('{}, está toda em maiusculas! \n '.format(resposta))
    else:
        print('{}, Não está toda em maiusculas! \n '.format(resposta))

    if resposta.islower() == True:
        print('{}, está toda em minusculas! \n '.format(resposta))
    else:
        print('{}, Não está toda em minusculas! \n '.format(resposta))
