def prn_parm1(arg):
    print(f'{arg}\n' * 2)


def prn_parm2(arg):
    print('ну все! сейчас напечатаю!')
    return (print(f'{arg}\n' * 2))


arg = input('введите чего нибудь -> ')

prn_parm1(arg)  # ввод значения в консоли
prn_parm1('привет')  # вызов функции с заданным параметро

prn_parm2('ку')
