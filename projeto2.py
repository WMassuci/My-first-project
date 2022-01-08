''''
Projeto: escreva um programa, que ao iniciar gera um valor aleatorio de 1 a 10 e permita que o usuario chute um numero ate que o valor aleatorio gerado no inicio do programa seja chutado novamente

o programa deve indicar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado

analisar criticamente o problema e descubra: basicamente se alguma parte consigo ou não entender,e buscar as informações....

1 - Quais são os dados de entrada necessarios?
   
   valor aleatorio, chute_numero

2 - o que devo fazer com esses dados?

  gerar o valor aleatorio, pedir que o usuario chute um valor, e verificar se o chute do usuario


3 - quais são os restriçoes deste problema ?

  deve entrar um valor do usuario

4 - qual é o resultado esperado?

  indicar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado

  
5 - qual é a sequencia de passos para chegar ao resultado esperado ? (o algoritmo)

input valor_aleatorio
input chute

if chute > valor_aleatorio
print(o chute foi acima)

if chute < valor_aleatorio
print(o chute foi abaixo)

if chute == valor_aleatorio
print(voce acertou)

'''

import random

valor_aleatorio = random.randint(1,10)

acertou = False

while acertou == False:
  chute = int(input('Informe um valor: '))

  if chute < valor_aleatorio:
    print('O Chute foi abaixo')

  if chute > valor_aleatorio:
    print('O Chute foi Acima')

  if chute == valor_aleatorio:
    acertou = True
    print('Voce acertou')


