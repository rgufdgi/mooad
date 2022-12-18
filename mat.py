import numpy as np

# обратная матрица
def inverse_matrix(arr):
    big_arr = np.hstack((arr, np.eye(len(arr))))  # расширенная матрица
    
    # проверка квадратности
    if arr.shape[0] != arr.shape[1]:
        print('Обратной матрицы не существует')
        return None
    
    # прямой ход
    for i in range(arr.shape[1]):
        elem = big_arr[i, i]  # диагональный элемент/первый ненулевой элемент
        big_arr[i] = big_arr[i] / elem  # для первой единицы в строке

        for j in range(i + 1, arr.shape[1]):
            elem1 = big_arr[j, i]  # элемент под диагональным, на который умножается первая строка
            big_arr[j] -= elem1 * big_arr[i]

    # обратный ход
    for i in range(arr.shape[1] - 1, -1, -1):
        relem = big_arr[i,i]  # нижний диагональный элемент
        big_arr[i] = big_arr[i]/relem  # для первой единицы в нижней строке
        
        for j in range(i - 1, -1, -1):
            elem2 = big_arr[j, i]
            big_arr[j] -= elem2 * big_arr[i]
            
    # срез с нужным куском матрицы
    rev_arr = big_arr[:,len(arr):]        
    return rev_arr

def returnB(X,Y):
    transx = np.transpose(X)
    helpfulmat1 = np.dot(transx, X)
    helpfulmat2 = inverse_matrix(helpfulmat1)
    helpfulmat3 = np.dot(helpfulmat2, transx)
    b = np.dot(helpfulmat3, Y)
    return b
 

# пример значений из лабораторной работы
epsilon = np.array([[0.0469], [0.0365], [0.0290], [0.0195], [0.0108]])  # y
n = np.array([[1, 6], [1, 5], [1, 4], [1, 3], [1, 2]])  # x

model = returnB(n, epsilon)

# среднее значение y
aver_y = 0
for i in range(len(epsilon)):
    aver_y += epsilon[i, 0]
aver_y /= len(epsilon)

# список значений полученной модели
model_y = []
b_0 = model[0, 0]
b_1 = model[1, 0]
for i in range(len(n)):
    m_y = b_0 + b_1 * n[i, 1]
    model_y.append(m_y)
    
# дисперсия модели
model_d = 0
for i in range(len(model_y)):
    elem_m = (epsilon[i, 0] - model_y[i]) ** 2
    model_d += elem_m
    
# дисперсия среднего
aver_d = 0
for i in range(len(model_y)):
    elem_a = (epsilon[i, 0] - aver_y) ** 2
    aver_d += elem_a
    
R = 1 - (model_d/aver_d)
Radj = 1 - (1 - R) * (4/3)

print(f'y = {b_0} + {b_1}x')
print(f'R = {R}, Radj = {Radj}')
    





    
    
    
    
    