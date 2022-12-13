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
    #print(big_arr)        
    return rev_arr
"""
def returnB(X,Y):
    try:
        transX = np.transpose(X)
        helpfulmat1 = inverse_matrix(np.dot(transX, X))
        helpfulmat2 = np.dot(helpfulmat1, transX)
        return np.dot(helpfulmat2, Y)
    except:
        print('что-то не так')
        return None
 """   
# l - количество наблюдений, n - количество признаков
x = np.array([[1, 3, 5, 4], [1, 7, 0, 8], [1, 11, 4, -3], \
              [1, 8, 7, -3], [1, 2, 4, 9]], dtype=np.float64)
y = np.array([2, 8, 9, 4, 6])

transx = np.transpose(x)
helpfulmat1 = np.dot(transx, x)
print(helpfulmat1)
helpfulmat2 = inverse_matrix(helpfulmat1)
print(helpfulmat2)
helpfulmat3 = np.dot(helpfulmat2, transx)
print(helpfulmat3)
b = np.dot(helpfulmat3, y)
print(b)

    
    
    
    
    
    