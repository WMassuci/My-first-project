'''
Projeto: Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".


analisar criticamente o problema e descubra: basicamente se alguma parte consigo ou não entender,e buscar as informações....

1 - Quais são os dados de entrada necessarios?

  velocidade_da_pessoa 

2 - o que devo fazer com esses dados?

  verificar se a pessoa esta entre a velocidade permitida ou nao

3 - quais são os restriçoes deste problema ?

  somente numeros

4 - qual é o resultado esperado?

  verificar se o usuario tomou  multa leve, grave ou gravíssima levando em consideração a velocidade maxima que é 80km
  
5 - qual é a sequencia de passos para chegar ao resultado esperado ? (o algoritmo)

input velocidade_usuario

if velocidade_usuario < 80
  print("nao ouve multa")

elif velocidade_usuario <= 90
  print("Levou multa leve")

elif velocidade_usuario > 90 and velocidade_usuario < 100
  print("Levou multa grave")

elif velocidade_usuario > 100
  print("Levou multa gravissima")

'''
velocidade_maxima = 80
verificar_novamente = 'SIM'

while verificar_novamente == 'SIM':

  velocidade_usuario = int(input('Informe sua velocidade: '))

  if velocidade_usuario <= velocidade_maxima:
    print("Não ouve multa")

  elif velocidade_usuario > velocidade_maxima and velocidade_usuario <= velocidade_maxima + 10:
    print("Levou multa leve")

  elif velocidade_usuario > velocidade_maxima + 11 and velocidade_usuario <= velocidade_maxima + 20:
    print("Levou multa grave")

  elif velocidade_usuario > velocidade_maxima + 20:
    print("Levou multa gravissima")

  verificar_novamente = input('Fazer a verificação novamente? [SIM/NAO]: ')
