import numpy as np
import statistics as st
import pandas as pd
from typing import Counter

print("Statistic Calc ∑ v1.0\n")

print("[1] * Medidas de Tendência Central")
print("[2] * Medidas de Dispersão")
print("[3] * Tabela - Classes")

keyIn = input("\n      Qual opção? -> ")

while keyIn != "1" or keyIn != "2" or keyIn != "3":
    if keyIn == "1":
        values = input("\n      Insira os valores: ").split(", ")
        lst = list(map(float, np.array(values)))

        media = st.mean(lst)
        moda = st.mode(lst)
        mediana = st.median(lst)

        order = sorted(lst)

        counter = Counter(lst)

        print(f"\n      Seq.    -> {order}")

        print("\n      Média   -> [%.2f]" % media)
        print("      Moda    -> [%.2f]" % moda)
        print("      Mediana -> [%.2f]" % mediana)

        print("      %s" % counter)
    elif keyIn == "2":
        values = input("\n      Insira os valores: ").split(", ")
        lst = list(map(float, np.array(values)))

        desvio_amostra = st.stdev(lst)
        variacao_amostra = st.variance(lst)  # amostra da população

        media = st.mean(lst)

        cv = ((st.stdev(lst) / st.mean(lst)) * 100)

        print("\n      Variância - A.          -> [%.2f]" % variacao_amostra)
        print("      Desvio-padrão - A.      -> [%.2f]" % desvio_amostra)

        print("\n      Média                   -> [%.2f]" % media)

        print(f"\n      Coeficiente de Variação -> [{cv:.2f}]")

    elif keyIn == "3":
        values = input("\n      Insira os valores: ").split(", ")
        lst = list(map(float, np.array(values)))

        variancia = input("Qual o intervalo? ")

    else:
        print("Digite uma entrada válida!")
        keyIn = input("\n      Qual opção? -> ")

# 7.9, 8.0, 7.2, 7.9, 10.9, 13.7, 13.1, 12.7, 12.2
# print(counter)
# print(lst)
# print(type(values))
# print(values)


# ---------------------------------------------------------------
        # print("\n      Amplitude        -> [%.2f]" % amplitude)

        # print("      Desvio Padrão    -> [%.2f]" % desvio_padrao)
        # print("      Desvio Absol.    -> [%.2f]" % desvio_absoluto)
        # print("      Variância        -> [%.2f]" % variancia)

        # print("      Covariância       -> [%.2f]" % covariancia)

        # amplitude = lst.max() - lst.min()

        # desvio_padrao = lst.std()
        # desvio_absoluto = lst.mad()
        # variancia = lst.var
        # covariancia = lst.cov()
