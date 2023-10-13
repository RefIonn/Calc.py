while True:
    def add(x, y):
        return x + y


    def sub(x, y):
        return x - y


    def mul(x, y):
        return x * y


    def div(x, y):
        return x / y


    op = input('Выберите операцию: ')
    if op in {'+', '-', '*', '/', ':'}:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        if b == 0 and op in {'/', ':'}:
            print('Нельзя делить на ноль')
        else:
            if op == '+':
                print(add(a, b))
            elif op == '-':
                print(sub(a, b))
            elif op in ['/', ':']:
                print(div(a, b))
            elif op == '*':
                print(mul(a, b))


    else:
        print('Incorrect operation')

    repeat = str(input('Хотите ли вы продолжить?: '))
    if repeat in {'Yes', 'Да', 'yes', 'да'}:
        continue  # Продолжение программы (цикла)
    else:
        break  # Выход из программы (цикла)

