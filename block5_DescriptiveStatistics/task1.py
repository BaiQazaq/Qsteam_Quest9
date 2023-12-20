# Calculate the mean, median, and mode of a given data set: [4, 8, 6, 9, 5, 2, 7].

some_lst = [4, 8, 6, 9, 5, 2, 7]
print(len(some_lst))

def mean(lst: list):
    sum_num = 0
    cnt = 0
    for i in lst:
        sum_num += i
        cnt += 1

    res = sum_num / cnt
    return res

def median(lst: list):
    lst.sort()
    if len(lst) % 2 == 0:
        if len(lst) == 2:
            return lst
        else:
            x = int(len(lst) / 2)
            new_lst = [lst[x-1], lst[x]]
            return new_lst
    else:
        x = int((len(lst) - 1) / 2)
        new_lst = [x]
        return new_lst

def mode(lst: list):
    count_dict = {}
    for i in lst:
        x = lst.count(i)
        if x > 1:
            count_dict[i] = x
    if count_dict != {}:
        mode_v = 1
        mode_k = 0
        for k, v in count_dict.items():
            if v > mode_v:
                mode_k = k
                mode_v = v
        print(f"The mode is -> {mode_k}")

    else:
        print("Mode absent, all units unique")
    


res_mean = mean(some_lst)
print(res_mean)
res_median = median(some_lst)
res_mode = mode(some_lst)