import numpy as np
import statistics as st
from typing import Counter

print("Statistic Calc ∑ v1.0\n")

print("[1] * Medidas de Tendência Central")
print("[2] * Medida de Dispersão")

keyIn = input("\nQual opção? -> ")

while keyIn != "1" or keyIn != "2":
    if keyIn == "1":
        values = input("Insira os valores: ").split(", ")
        lst = list(map(float, np.array(values)))

        media = st.mean(lst)
        mediana = st.median(lst)
        moda = st.mode(lst)

        counter = Counter(lst)
    elif keyIn == "2":
        values = input("Insira os valores: ").split(", ")
        lst = list(map(float, np.array(values)))

        amplitude = lst.max() - lst.min
        variancia = lst.var
        desvio_padrao = lst.std()
        desvio_absoluto = lst.mad()
        covariancaia = lst.cov()
    else:
        print("Digite uma entrada válida!")
        keyIn = input("\nQual opção? -> ")


# print(counter)
# print(lst)
# print(type(values))
# print(values)
