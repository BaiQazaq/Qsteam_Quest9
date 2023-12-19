# Calculate the probability of testing positive for a disease given a 5% false positive rate and a 0.1% infection rate in the population.
# Use Bayes' theorem to update the probability of having a disease based on a positive test result.


# Оценка вероятности достоверности медицинского
# (биохимического) теста
# Предположим, что некоторый тест правильно предсказывает
# наличие или отсутствие определенного заболевания с вероятностью
# 0,95 .
# Это значит, что если человек действительно болен, то тест
# дает положительный результат с вероятностью 0,95, а с
# вероятностью 0,05 тест дает отрицательный результат.
# Если же человек здоров, то тест с вероятностью 0,95 дает
# отрицательный результат, а с вероятностью 0,05 тест дает
# положительный результат.
# 1% населения имеет это заболевание.
# Предположим, что Вы прошли тестирование и получили
# положительный результат. Какова вероятность того, что вы
# действительно больны?
# Итак, вспомним некоторые понятия из теории вероятностей.

# *************Условная вероятность*****************
# Известно, что событие В произошло.
# Какова вероятность того, что
# произошло событие А ?
# Условная вероятность события А при
# условии, что произошло событие В:

#          𝑛(𝐴𝐵)    𝑛(𝐴𝐵)/𝑛     𝑃(𝐴𝐵)
# 𝑃 (𝐴|𝐵) =----- = --------- = ------
#           𝑛(𝐵)    𝑛(𝐵)/𝑛      𝑃(𝐵)

# Если 𝑃(𝐴|𝐵) = 𝑃(𝐴) , то 𝑃(𝐴𝐵) = 𝑃(𝐴)𝑃(𝐵), следовательно,
# А и В – независимые события.

# ************************Формула Байеса************************
# 𝐴1, ⋯ , 𝐴𝑛 – полная группа событий,
#                   𝑛
# 𝐴𝑖𝐴𝑗 = ∅ , 𝑖 ≠ 𝑗,  U  𝐴𝑖 = Ω
#                  𝑖=1
# Формула полной вероятности:
#           n           n
#   𝑃(𝐵) = SUM 𝑃(𝐵𝐴𝑖) = SUM 𝑃(𝐵|𝐴𝑖)𝑃(𝐴𝑖)
#          𝑖=1          𝑖=1

# Формула Байеса
#                 𝑃(𝐴𝑖𝐵)     𝑃(𝐵|𝐴𝑖)𝑃(𝐴𝑖)
#       𝑃(𝐴𝑖|𝐵) = ------- = ------------
#                  𝑃(𝐵)         𝑃(𝐵)

# Обозначим события:
# 𝐴1 – вы больны,
# 𝐴2 – вы здоровы,
# 𝐵 – тест положительный.

# 𝑃(𝐵|𝐴1) = 0,95 ,  𝑃(𝐵|𝐴2) = 0,05
# 𝑃(𝐴1) = 0,01 ,    𝑃(𝐴2) = 0,99

# 𝑃(𝐵) = 𝑃(𝐵|𝐴1) * 𝑃(𝐴1) + 𝑃(𝐵|𝐴2) * 𝑃(𝐴2) =
# 0.95 ∙ 0.0001 + 0.05 ∙ 0.9999 = 0.05009                                   |                # = 0,95 ∙ 0,01 + 0,05 ∙ 0,99 = 0,059
#                                                                           |
#             𝑃(𝐵|𝐴1) ∙ 𝑃(𝐴1)    0,95 ∙ 0,0001                              |                𝑃(𝐵|𝐴1) ∙ 𝑃(𝐴1)    0,95 ∙ 0,01
#  𝑃(𝐴1|𝐵) = --------------- = ------------- ≈  0.0018965861449391096       |      𝑃(𝐴1|𝐵) = --------------- = ------------- ≈ 0,161
#                   𝑃(𝐵)           0.05009                                  |                       𝑃(𝐵)             0,059
#                                                                           |
# Таким образом, несмотря на положительный результат теста, вы в            |
# реальности имеете это заболевание всего лишь с вероятностью               |
# 0,0019, а с вероятностью 0,9981 вы здоровы                                |                   0,16, а с вероятностью 0,84 вы здоровы

def full_probability(pa1, pba2):
    # 𝑃(𝐵) = 𝑃(𝐵|𝐴1) * 𝑃(𝐴1) + 𝑃(𝐵|𝐴2) * 𝑃(𝐴2)
    p_ba1 = 1 - pba2
    p_a2 = 1 - pa1
    p_b = p_ba1 * pa1 + pba2 * p_a2
    print(f"***** = {p_ba1} * {pa1} + {pba2} * {p_a2} = {p_b}")
    return p_b, p_ba1

def bayece(pa1, pba2):
#            𝑃(𝐵|𝐴1) ∙ 𝑃(𝐴1)   
# 𝑃(𝐴1|𝐵) = --------------- 
#                 𝑃(𝐵)            
    p_b, p_ba1 = full_probability(pa1, pba2)
    p_a1b = p_ba1 * pa1 / p_b
    return p_a1b

ill = 0.0001
false_positive = 0.05

res = bayece(ill, false_positive)
print(res)
