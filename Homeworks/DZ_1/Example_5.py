# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


Abcissa_1=float(input('Введите координату по оси х для первой точки'))
Ordinata_1=float(input('Введите координату по оси y для первой точки'))
Abcissa_2=float(input('Введите координату по оси х для второй точки'))
Ordinata_2=float(input('Введите координату по оси y для второй точки'))

result=((Abcissa_2 - Abcissa_1) ** 2 + (Ordinata_2 - Ordinata_1) ** 2) ** 0.5
print('Расстояние между точками:')
print(result)