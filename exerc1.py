'''
Exercício 1-) Fazer um programa que receba o peso de 7 pessoas - Calcular e mostrar :
* Quantidade de pessoas acima de 90kg
* A média dos pesos das pessoas
'''

p_pessoas=[]
n_pessoas=0
for i in range(7):
    p_pessoas.append(float(input("Digite o peso em KG da "+str(i+1)+"ª pessoa: ")))
    if p_pessoas[i] > 90:
        n_pessoas +=1

for y in range(7):
    m_pessoas+=p_pessoas[y]

m_pessoas/=7

print(f'Existem {n_pessoas} acima dos 90KG e a média de todos os pesos é de {round(sum(p_pessoas)/7,2)}KG')