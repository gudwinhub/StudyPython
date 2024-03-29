lst = [['*', '*'], [], []]
lst1, lst2, lst3 = [*lst]
lst1.extend('*')  # можно использовать метод append() результат тот же
lst2.append(['*'] * 3)
lst3.append(['*'] * 3)
print(lst1, lst2, lst3)
