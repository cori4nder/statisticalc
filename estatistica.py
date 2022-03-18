import numpy as np
import statistics as st
import pandas as pd
from typing import Counter

print("Statistic Calc ∑ v1.0\n")

print("[1] * Medidas de Tendência Central")
print("[2] * Medidas de Dispersão")

keyIn = input("\n      Qual opção? -> ")

while keyIn != "1" or keyIn != "2":
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

    else:
        print("      Digite uma entrada válida!")
        keyIn = input("\n      Qual opção? -> ")
