#criar um fatorial de um numero
#primeiro utilizar o metodo 5q's
''''
#0.1 - analisar criticamente o problema e descubra: basicamente se alguma parte consigo ou não entender,e buscar as informações....

#1 - Quais são os dados de entrada necessarios?
  # um numero

#2 - o que devo fazer com esses dados?
  # fazer a fatorial do numero

#3 - quais são os restriçoes deste problema ?
  # o numero não pode ser negativo e nem real, apenas positivos e inteiros

#4 - qual é o resultado esperado?
  # o resultado esperado é mostrar o resultado do faturial do numero

#5 - qual é a sequencia de passos para chegar ao resultado esperado ? (o algoritmo)
  
  input numero
  if numero > 0
  if numero = inteiro

  fatorial = 1
  loop 1 a numero
    fatorial = fatorial * numero
  
  print(fatorial)

'''


numero = int(input('Informe um numero: '))

if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
print(fatorial)