'''
Exercício 4-) Faça um programa que receba várias idades e calcule e mostre a média das idades. Finalize o programa quando a entrada for igual a -1
'''

pessoas = []
contador = 0
flag = 0
while flag != 1:
    pessoas.append(int(input('Digite a idade da '+str(contador+1)+'ª pessoa: ')))
    if pessoas[contador] <= -1:
        pessoas.pop(contador)
        flag = 1
    else:
        contador +=1
print(f'A média da idade das pessoas digitadas é de {round(sum(pessoas)/contador,2)}') 