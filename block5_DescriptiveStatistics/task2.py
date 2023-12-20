# What is the range of the dataset [5, 2, 8, 9, 12, 3]?

# Чтобы найти размах набора данных [5, 2, 8, 9, 12, 3], нужно вычесть минимальное значение из максимального значения.

# Упорядочим набор данных: [2, 3, 5, 8, 9, 12].

# Теперь найдем размах:

#       Размах = Максимальное значение − Минимальное значение

#       Размах=12−2=10

# Таким образом, размах набора данных [5, 2, 8, 9, 12, 3] равен 10.

lst = [5, 2, 8, 9, 12, 3]

def range(lst: list):
    max_num = max(lst)
    min_num = min(lst)
    range_num = max_num - min_num
    return range_num

res = range(lst)
print(res)