# Calculate the probability of drawing 2 Queens and 1 Ace in a three-card hand from a standard deck.

# Чтобы вычислить вероятность вытянуть 2 Дамы и 1 Туз в руке из трех карт из стандартной колоды, вы можете использовать комбинаторику.
# Общее количество способов выбрать 3 карты из стандартной колоды (без учета порядка) задается формулой 
#         C(52,3), 
    
#     где C(52,3) - количество сочетаний 52 карт по 3.

# Количество способов выбрать 2 Дамы из 4 Дам в колоде равно 
# C(4,2), 

# и количество способов выбрать 1 Туз из 4 Тузов равно 
# C(4,1).

# Вероятность (P) может быть вычислена следующим образом:
    
#             P(2 Дамы и 1 Туз) = ( C(4,2) × C(4,1) ) / C(52,3)

# Давайте вычислим:

#                                    4!          4!  
#                                 2!(4−2)!    1!(4−1)!        
#             P(2 Дамы и 1 Туз) = ----------------------
#                                           52!
#                                        3!(52−3)!

# Подставим значения:
#                                     24          24
#                                     2           3
#             P(2 Дамы и 1 Туз)= ------------------------
#                                         23426
#                                           6
# ​
            
#                                     12           8            
#             P(2 Дамы и 1 Туз)= -------------------------
#                                          3905


#                                           96
#             P(2 Дамы и 1 Туз)≈ -------------------------
#                                          3905

#             P(2 Дамы и 1 Туз)≈ 0,0246

# Таким образом, вероятность вытянуть 2 Дамы и 1 Туз из трех карт из стандартной колоды составляет примерно 0,0246 или 2,46%.

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

def task_solving(deck, set_cards, quees_draw, ace_draw, total_draw):
    p_quees = P_solving(set_cards, quees_draw)
    p_ace = P_solving(set_cards, ace_draw)
    p_total = P_solving(deck, total_draw)
    print(f"p_quees = {p_quees}, \n p_ace = {p_ace}, \n p_total = {p_total}")
    all_probability = p_quees * p_ace / p_total
    return all_probability

deck = 52
set_cards = 4
quees_draw = 2
ace_draw = 1
total_draw = quees_draw + ace_draw

res = task_solving(deck, set_cards, quees_draw, ace_draw, total_draw)
print(res)

#  p_quees = 6.0, 
#  p_ace = 4.0, 
#  p_total = 22100.0
#  0.0010859728506787331