# Numpy é abreviação de numerical python. É uma biblioteca desenvolvida para otimizar calculos cientificos
# e é grandemente mais veloz do que lista do python, por exemplo, por vários motivos. Foi construída em linguagem C,
# uma linguagem de baixo nível. Os algoritmos do NumPy utilizam arrays multidimensionais otimizados para cálculos
# estatísticos, matemáticos e de álgebra linear.

import time
import numpy as np

x = np.random.random(10000000)


def calc_time_py(x):
    start = time.time()
    mean = sum(x) / len(x)
    return time.time() - start


def cal_time_numpy(x):
    start = time.time()
    mean = np.mean(x)
    return time.time() - start


time_py = calc_time_py(x)
print(time_py)

time_numpy = cal_time_numpy(x)
print(time_numpy)
