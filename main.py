print('Введите коэффициенты для уравнения:')

a = float(input('Какое a? '))
b = float(input('Какое b? '))
c = float(input('Какое c? '))

discr = b ** 2 - 4 * a * c
print('Дискриминант равен', discr)

if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)

    print('Первый корень', x1)
    print('Второй корень', x2)
elif discr == 0:
    x3 = -b / (2 * a)

    print('Корень', x3)
else:
    print('Нет корней')