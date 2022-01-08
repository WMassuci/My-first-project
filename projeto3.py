'''
Projeto: Realizar o desconto de 20% da compra somente quando, o valor da compra for maior que 200 reais

analisar criticamente o problema e descubra: basicamente se alguma parte consigo ou não entender,e buscar as informações....

1 - Quais são os dados de entrada necessarios?
   
   dado do valor da compra
   dado do desconto

2 - o que devo fazer com esses dados?

  comparar se o valor da compra é maior que 200 para aplicar o desconto

3 - quais são os restriçoes deste problema ?

  é necessario informar o valor da compra

4 - qual é o resultado esperado?

  verificar que ouve o desconto, e aplica-lo no valor final da compra
  
5 - qual é a sequencia de passos para chegar ao resultado esperado ? (o algoritmo)

input valor_compra
input desconto

if valor_compra > 200
  novo_preco = valor_compra - (valor_compra * 20/100)
  print(o valor final foi novo_preco)

if valor_compra < 200
  print(sem desconto, valor é o mesmo)

if valor_compra == 200
  print(sem desconto, o valor continua o mesmo)

'''
finalizou = 'NAO'

while finalizou == 'NAO':

  valor_compra = float(input('Informe o valo da compra: '))

  if valor_compra > 200:
    novo_preco = valor_compra - (valor_compra * 20/100)
    print('Valor da compra R${}'.format(valor_compra))
    print('Desconto Aplicado: 20%')
    print('Valor Final R${}' .format(novo_preco))

  if valor_compra < 200:
    print('Valor da compra R${}'.format(valor_compra))
    print('Desconto Aplicado: 0%')
    print('Valor Final R${}' .format(valor_compra))

  if valor_compra == 200:
    print('Valor da compra R${}'.format(valor_compra))
    print('Desconto Aplicado: 0%')
    print('Valor Final R${}' .format(valor_compra))

  finalizou = input('Compra Finalizada?[SIM/NAO] ')