'''
Exercício 3-) Faça um programa que verifique e mostre os números entre 1000 e 2000(inclusive) que, quando dividido por 11, produz um resto igual à 5
'''
lista=[]

for i in range(1000,2001):
    if (i%11) == 5:
        lista.append(i)
print(str(lista))