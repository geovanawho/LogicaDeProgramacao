num = int(input('Escolha um numero: '))
num2 = int(num * 3) + 1
num3 = int(num * 2) - 1
soma = int(num2+num3)

print('A soma de {} com o antecessor de seu tripo ({}) e o antecessor de seu dobro ({}) é {}.'.format(num, num2, num3, soma))
