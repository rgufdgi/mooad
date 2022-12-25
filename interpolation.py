# интерполяция полиномом Лагранжа

def koef(x_list, i, x):  # коэффициенты полинома (произведения) 
    product = 1
    divider = 1
    for j in range(len(x_list)):
        if j != i:
            product *= x - x_list[j]
            divider *= x_list[i] - x_list[j]
        else:
            continue
    return product / divider

def l_interpolation(x_list, y_list, x):  # вычисление значения функции в точке x
    summ = 0
    koef_list = []
    for i in range(len(x_list)):
        elem = koef(x_list, i, x)
        koef_list.append(elem)
    for i in range(len(x_list)):
        summ += y_list[i] * koef_list[i]
    return summ

# интерполяция полиномом Ньютона
def div_differences(x_list, y_list, k):  # функция для разделенной разности
    summ = 0
    for i in range(k + 1):
        divider = 1
        for j in range(k + 1):
            if j != i:
                divider *= (x_list[i] - x_list[j])
        summ += y_list[i] / divider
    return summ

def n_interpolation(x_list, y_list, x):  # вычисление значения функции в точке x
    elems = []
    for i in range(1, len(x_list)):
        elem = div_differences(x_list, y_list, i)
        elems.append(elem)
        
    result = y_list[0]
    for i in range(1, len(y_list)):
        product = 1
        for j in range(i):
            product *= (x - x_list[j])
        result += elems[i - 1] * product
    return result
            
        
# пример значений
x_elements = [-9, 12, 33, 54, 75]
y_elements = [500, -5, -21, -34, -518]

# проверка
for c in x_elements:
    print(l_interpolation(x_elements, y_elements, c))
    print(n_interpolation(x_elements, y_elements, c))

