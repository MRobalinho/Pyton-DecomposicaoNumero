# Autor: Manuel Robalinho
# crie um programa em Python que leia um número inteiro menor que 1000 e
#imprima a quantidade de centenas, dezenas e unidades do mesmo,

# pede um n. entre 0 e 999
print('----  Separar Centenas, Dezenas e Unidades de um numero ----')
number_1 = int(input('Insira um numero menor que 1000 :'))

# valida numero < 1000 e separa centenas , dezenas e unidades
if number_1 < 1000:
    print('--- Resultado: ----')
    centenas = int(number_1 / 100)
    resto    = number_1 - (centenas*100)
    dezenas  = int(resto / 10)
    unidades = resto - (dezenas*10)
 
    print('São ', centenas, ' Centenas, ', dezenas, ' dezenas e ', unidades, ' unidades')
   # print('Centenas: ', centenas)
   # print('Dezenas : ', dezenas)
   # print('Unidades: ', unidades)
   # print('---------------')
else:
    print('Não indicou um numero menor que 1000, por favor corra novamente o programa.')


