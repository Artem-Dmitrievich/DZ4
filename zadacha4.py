from random import randint
from sympy import symbols
# https://pythonru.com/biblioteki/sympy-v-python : для выполнения символьных вычислений.
# Sympy - многочлены, мат.анализ, дискретная мат-ка, матрицы, геометрия, построение графиков, физика, статистика.
# Symbols - может определять несколько символов одновременно
from math import prod
# Функция prod() вычисляет произведение элементов массива, которое так же может выполняться по указанной оси (осям).

max_val = 100 # максимальное значение
k = int(input('Введите натуральную степень k:'))
# коэфф. при макс.значеии не должен быть равен 0
koeff = [randint(-max_val, max_val) for i in range(k)] + [randint(1, max_val)]
x = symbols('x')

print(sum(map(prod, zip(koeff, [x ** i for i in range(k + 1)]))), '= 0')
