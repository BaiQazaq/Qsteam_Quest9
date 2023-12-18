# Чтобы вычислить вероятность угадать ровно 3 числа в лотерее, где из 60 чисел вытягивают 6, 
# можно использовать формулу биномиального распределения.

# Вероятность угадать 3 числа (P) при 
# n = 6 (всего 6 попыток), 
# k = 3 (угадывание ровно 3 чисел) и 
# p = 1/10 (вероятность угадывания одного числа) может быть вычислена по формуле:

#         P(k,n,p) = C(n,k) × p^k × (1−p)^n−k
# где 
#     C(n,k) - это количество сочетаний из n по k.

#                 n!
#     C(n,k)= -----------
#               k!(n−k)!

# Давайте вычислим это:

#                  1                1        9
#         P(3, 6, ---) = C(6, 3) × (--)^3 ​× (--)^3
#                  10               10       10

        
#                  1        6!        1        9
#         P(3, 6, ---) = --------- × (--)^3 ​× (--)^3
#                  10    3!(6 - 3)!   10       10​

# Теперь мы можем подставить значения:

#                  1        20          1        729
#         P(3, 6, ---) = --------- × (-----) ​× (-----)
#                  10        1         1000      10​00


#                   1      14580    
#         P(3, 6, ---) = --------- = 0,01458
#                  10     1000000

# Таким образом, вероятность угадать ровно 3 числа из 6 в лотерее из 60 чисел составляет примерно 0,01458 или 1,458 %.

# In a lottery where 6 numbers are drawn from 60, what is the probability of guessing exactly 3 numbers correctly?

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def P_solving(n, k):
    """C(n,k)= n! / k!(n−k)!"""
    numerator = factorial(n)
    denominator_k = factorial(k)
    denominator_n_k = factorial(n-k)
    probability = numerator / (denominator_k * denominator_n_k)
    return probability

def task_solving(k, n, total):
    p = n / total
    """ P(k,n,p) = C(n,k) × p^k × (1−p)^n−k"""
    probability_nk = P_solving(n, k)
    res_pk =  p ** k
    res_1p = (1 - p) ** (n - k)
    P_result = probability_nk * res_pk * res_1p
    return P_result

    

total_num = 60
drawn_num = 6
corect_num = 3

result = task_solving(corect_num, drawn_num, total_num)
print(result)

#0.014580000000000004