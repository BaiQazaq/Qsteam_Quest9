# Calculate the variance and standard deviation of the numbers [3, 7, 8, 5, 12].
# Для вычисления дисперсии и стандартного отклонения для набора чисел [3, 7, 8, 5, 12], следуем следующим шагам:

# Среднее значение (Mean):
#           3+7+8+5+12     35
# Среднее= ------------ = ---- = 7
#               5           5

# Дисперсия (Variance):
# Дисперсия измеряет, насколько каждое число в наборе отличается от среднего. Формула для дисперсии:
#                        n         −
#                       ∑    (Xi - X)^2
#                        i=1
#           Дисперсия= ------------------
#                               n
# где 
# Xi - каждое число в наборе, 

# ˉ
# X - среднее значение, 

# n - количество чисел в наборе.

# Рассчитаем:
#                   (3−7)^2 + (7−7)^2 + (8−7)^2 + (5-7)^2 + (12-7)^2 
#       Дисперсия= --------------------------------------------------
#                                           5
#                    16 + 0 + 1 + 4 + 25
#       Дисперсия = ---------------------
#                             5
 
#                    46
#       Дисперсия = ---- = 9.2
#                     5

# Стандартное отклонение (Standard Deviation):
# Стандартное отклонение - это квадратный корень из дисперсии. 
#
# Стандартное отклонение = sqrt(9.2) ≈ 3.04


# Итак, для набора чисел [3, 7, 8, 5, 12]:

# Дисперсия: 9.2
# Стандартное отклонение: примерно 3.04
from math import sqrt
lst = [3, 7, 8, 5, 12]

def mean(lst: list):
    sum_num = 0
    cnt = 0
    for i in lst:
        sum_num += i
        cnt += 1

    res = sum_num / cnt
    return res

def variance(lst: list):
    mean_num = mean(lst)
    var_lst = []
    len_num = len(lst)
    for i in lst:
        x = (i - mean_num) ** 2
        var_lst.append(x)
    var_res = sum(var_lst) / len_num
    return var_res

def standard_deviation(var: int):
    res_std_dev = sqrt(var)
    return res_std_dev

res_var = variance(lst)
res_std_dev = standard_deviation(res_var)

print(f"Итак, для набора чисел {lst}:")
print(f"Дисперсия: {res_var}")
print(f"Стандартное отклонение: {res_std_dev}")
