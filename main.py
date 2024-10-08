""" 
Задана рекуррентная функция. 
Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант №20: 
F(1) = 1; G(1) = 1; F(n) = (-1)n*(F(n–1) – 2*G(n–1))/(2n)!
G(n) = F(n–1) + G(n–1), при n >=2 
"""
import time
import matplotlib.pyplot as plt
from functools import lru_cache

n = -1

timer=[]
timer_rec=[]
fact = [1] * 2

one = -1

lru_cache(maxsize=None)
def itfact(x):
    global fact
    if fact[1] < x:
        for i in range(fact[1]+1, x+1):
            fact[0] = fact[0] * i
    elif fact[1] > x:
        for i in range(x+1, fact[1]+1):
            fact[0] = fact[0] // i
    fact[1] = x
    return fact[0]


#рекурсия
#F(n) = (-1)n*(F(n–1) – 2*G(n–1))/(2n)!
lru_cache(maxsize=None)
def rec_f(x):
    global one
    one *= -1
    if x < 2:
        return 1
    else:
        return one*((rec_f(x-1) - 2*rec_g(x-1))/itfact(x*2))

#G(n) = F(n–1) + G(n–1)
lru_cache(maxsize=None)
def rec_g(x):
    if x < 2:
        return 1
    else:
        try:
            return rec_f(x-1) + rec_g(x-1)
        except ZeroDivisionError:
            #print("Ошибка деления на ноль (float нехватает знаков после запятой)")
            return 1
#F(n) = (-1)n*(F(n–1) – 2*G(n–1))/(2n)!
def it_f(x):
    global one
    f = [1, 1]
    g = [1, 1]
    for i in range(1,x+1):
        one *= -1
        try:
            g[1] = f[0] + g[0]
        except ZeroDivisionError:
            #print("Ошибка деления на ноль (float нехватает знаков после запятой)")
            g[1] = 1
        f[1] = one*((f[0] - 2*g[0])/itfact((i+1)*2))
        f[0], f[1] = f[1], f[0]
        g[0], g[1] = g[1], g[0]

    return f[1]

while n < 1:
    print("Введите натуральное число от 1 ")
    n = int(input())

graf = list(range(1, n+1))

for i in graf:
    start = time.time()
    one = -1 if i % 2 == 0 else 1
    result = it_f(i)
    end = time.time()
    timer.append(end-start)
    start_rec = time.time()
    one = -1
    res = rec_f(i)
    end_rec = time.time()
    timer_rec.append(end_rec-start_rec)
    print(i,
          " | Результат рекурсии ->", res,
          " | результат итерации ->", result,
          " | время  рекурсии ->", end_rec-start_rec,
          " | время  итерации ->",end-start)

plt.plot(graf, timer, label='Итерационная функция.')
plt.plot(graf, timer_rec, label='Рекусионная функция.')
plt.legend(loc=2)

plt.xlabel('Значение n')
plt.ylabel('Время выполнения (c)')
plt.show()
