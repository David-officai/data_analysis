# variance and standard deviation

import numpy as np

data_list = []

num = int(input("how many >> "))

for i in range(num):
    data = int(input("Type any data >> "))   
    data_list.append(data) 

ave = sum(data_list) / len(data_list)

def variance () :
    data_sq = [i**2 for i in data_list]
    ave_sq = sum(data_sq) / len(data_list)
    return ave_sq - ave**2

def standard_deviation () :
    return np.sqrt(variance())


print("平均 : " + str(ave))
print("分散 : " + str(variance()))
print("標準偏差 : " + str(standard_deviation()))
