n = int(input('введите количество чисел для ряда Фибоначи -> '))
fib1 = fib2 = 1

# подсчет чисел ряда Фибоначи через цикл for
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

# подсчет чисел ряда Фибоначи через цикл while
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print('Значение этого элемента:', fib2)
