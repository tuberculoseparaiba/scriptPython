# -*- coding: utf-8 -*-
"""
Criado Segunda-feira, 05 de fevereiro de 2018

@author: Kleyton Klaus Guedes de Souza
===============================================
Gerador de Distribuição de Frequências
+++++++++++++++++++++++++++++++++++++++++++++++
"""

import matplotlib.pyplot as plt
from numpy import genfromtxt

dados = genfromtxt('tx_incidencia_tuberculose.csv')
histograma1 = plt.hist(dados, bins="sturges")
#histograma2 = plt.hist(dados, bins="scott")
#histograma3 = plt.hist(dados, bins="fd")
histograma4 = plt.hist(dados, bins= 3)
#histograma5 = plt.hist(dados)