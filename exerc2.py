'''
Exercício 2-) Fazer um programa que mostre o resultado de n!

5! = 5 * 4 * 3 * 2 * 1  
'''

'''
Primeira tentativa
'''
n = int(input('Digite o valor de n!: '))
lista = []
result = 1

for i in range(n+1):
    lista.append(i)
    msg += str(lista[i])+'*'

lista.pop(0)
print(lista)

for y in range(n):
    result *= lista[y] 
print(result)

'''
Otimização
'''
n = int(input('Digite o valor de n!: '))
resultado = 1

for i in range(n,0,-1):
    resultado *= i

print(resultado)