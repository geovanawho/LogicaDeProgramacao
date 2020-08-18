num1 = int(input('Insira o primeiro numero: '))
num2 = int(input('Insira o segundo numero: '))
num3 = int(input('Insira o terceiro numero: '))

som1 = int(num1 **2)
som2 = int(num2 **2)
som3 = int(num3 **2)

total = som1+som2+som3

print('A soma dos quadrados dos numeros {}, {} e {} é {}.'.format(num1, num2, num3, total))
