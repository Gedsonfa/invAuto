from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

data_inicial = date(2000, 1, 1)

data_final = date(2022, 3, 31)

taxas_selic = sgs.get({"selic":11}, start= data_inicial, end = data_final)/100

janela = ((1 + taxas_selic).rolling(window = 500).apply(np.prod) - 1)

janela = janela.reset_index()

janela["data_inicial"] = janela["Date"].shift(500)

janela = janela.dropna()

janela.columns = ["data_final", "retorno_selic", "data_inicial"]

maior_retorno = janela["retorno_selic"].max()

gabarito = janela[janela["retorno_selic"] == maior_retorno]

print(gabarito)