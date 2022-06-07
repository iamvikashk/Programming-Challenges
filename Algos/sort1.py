"""This is a simple sorting algorithm. It is slower than Python sorted function as the size of list increases and needs improvement """


def is_sorted(lst):
    for j in range(len(lst) - 1):
        if lst[j] <= lst[j + 1]:
            pass
        else:
            out = False
            break
        out = True
    return out


def sorting(lst):
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            pass
        else:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
    if not is_sorted(lst):
        sorting(lst)
    return lst


lst = [0.5488135, 0.71518937, 0.60276338, 0.54488318, 0.4236548, 0.64589411, 0.43758721, 0.891773, 0.96366276,
       0.38344152]

print(sorting(lst))
