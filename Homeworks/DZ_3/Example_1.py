# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def summa_nech_positions(numbers): #def-помогает сообщить что мы вызываем функцию
    s = 0
    for i in range(len(numbers)): #Узнать количество символов (длину строки) можно при помощи функции len 
        if i % 2 != 0:
            s += numbers[i]
    print('Сумма равна:')
    print(s)

numbers = []
summa_nech_positions(numbers)
numbers = list(map(int, input("Введите числа через пробел:\n").split())) #map-это встроенная функция, которая применяет функцию ко всем входным элементам итератора
summa_nech_positions(numbers)