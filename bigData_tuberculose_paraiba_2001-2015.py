# -*- coding: utf-8 -*-
"""

Script Desenvolvido para Mineraçao de Dados do Dataset base_tuberculose_paraiba_2001-2015_.csv
Objetivo: Minerar Regras Associativas sobre os Casos de Tuberculose na Paraiba, no Periodo de
2001 a 2015, com dados proveniente do Sage Saude e do IBGE.

O dataset seguiu como regra de exclusao municipios que durante 10 anos ou mais nao apresentaram
Taxa de Incidencia de Tuberculose, portanto, dos 223 municipios da Paraiba, ficaram para analise
apenas 146 municpios. Essa medida foi adota, pois, nao e possivel averiguar se esse municipios
tiveram casos 0 de tuberculose durante estes anos, ou, se apenas os dados nao foram consolidados
e enviados para os sistema que compoes o SAGE Saude. Utilizar estes municipios com parametros
poderia tendencia o processo de aprendizagem do algoritimo apriori e gerar regras longes da
realidade da amostra.

Criado Segunda-feira, 05 de fevereiro de 2018

@author: Kleyton Klaus Guedes de Souza
"""



import pandas as pd

#=====================================================================#
#Primeiro passo, Ler o arquivo CSV, utilizando a biblioteca pandas.
#Onde será criado uma váriavel com um dataframe com os dados do csv
#=====================================================================#

# Importa arquivo csv sem cabeçalho (header)
dados = pd.read_csv('tuberculose_paraiba_2001-2011_final.csv', header = None)

#Busca  Dimensões do Dataframe linhasxcoluas dimensoes[]
dimensoes = dados.shape

#=====================================================================#
#Armazena os dados do dataframe em um list do python, para, ser 
#utilizado no algoritomo apyori
#=====================================================================#

#Ler o Dataframe e armazena-lo em uma lista, chamada transacoes

transacoes = []

for i in range(0, dimensoes[0]):
    transacoes.append([str(dados.values[i, j]) for j in range(0, dimensoes[1])])
    

#=====================================================================#
#Aplicando regras de associação apriori nas transações salvas a partir 
#do csv
#=====================================================================#

#Gerar Regras de Associação    
from apyori import apriori

#Criar Regras Sem Definir Suporte e Confiança
#Sintax-> apriori(dadosTransacionais, min_support, min_confidence, min_lift, min_length (quantidade minima de produtos relacionados))
regras = apriori(transacoes, min_support = 0.1, min_confidence = 0.6    , 
                 min_lift = 2, min_length = 2)


#=====================================================================#
#Exibindo Regras Geradas com o apriori
#do csv
#=====================================================================#
#Armazenando as Regras Geradas

resultados = list(regras)

#Exibir Regras de Associação Geradas
#resultados

#Refinando a Exibição das Regras de Associação
print()
print("Resultado Refinado")
print()

resultados2 = [list(x) for x in resultados]
#print (resultados2)

#Exibir Resultado Formatado
#Refinando a Exibição das Regras de Associação
print()
print("Resultado Refinado")
print()

resultadoFormatado = []
# O range é definido de 0 a 3, ou seja, caso existam 4 Regras, elas serão
#Exibidas, nesse exemplo existem 38, mas, só são exibidas 4
for j in range (0,42):
    #Em resultados [j][2] busca-se os valores da confiança e do lift
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])

print (resultadoFormatado)
