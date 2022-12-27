# распределение непрерывных величин
import matplotlib.pyplot as plt

#функция распределения
def f(x):
    if x < -1:
        return 0
    if x > 1:
        return 1
    else:
        return 0.125 * (x + 1)**3

a = -2  # левый предел интегрирования
c = -1
d = 1
b = 2  # правый предел интегрирования

# численное интегрирование
n = 25  # число разбиений
cycle = [a, c, d, b]
summ = 0
X = []  # значения для
Y = []  # построения графика

for i in range(1,len(cycle)):
    x = (cycle[i]-cycle[i-1])/n
    fa = f(cycle[i-1])
    fb = f(cycle[i])
    if cycle[i] != d:
        fa = 0
        fb = 0
    j = 1
    Sum = 0
    while(j < n):
        m = cycle[i-1] + j*x  # значение на оси х
        Sum = Sum + 2*f(m)  # значение на оси y
        j = j + 1
        if cycle[i] != d:
            Sum = 0
        X.append(x*Sum/2+summ)
        Y.append(m)
    summ = (fa + Sum + fb)*x/2
    
# построение графика
plt.plot(Y, X, '.-')
plt.show()

