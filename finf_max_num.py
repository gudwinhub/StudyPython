def find_max(*args):
    global max_num
    k = n = len(args)
    max_num = args[k - 1]
    print(*args)
    if not args:
        return print('вы забыли ввести числа')
    if n == 1:
        max_num = args[0]
        print(max_num)
        return max_num
    else:
        # if n > 1:
        n -= 1
        max_num = args[n]
        num_tmp = args[n - 1]
    if max_num >= num_tmp:
        args = list(args)
        # args[n-1] = max_num
    else:
        max_num = num_tmp
    find_max(*args[:n])


a = find_max(11, 47, 55, 25, 37)
# b = find_max(2)
print(type(a), ' ', a)
