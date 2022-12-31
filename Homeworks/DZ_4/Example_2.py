# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

# n=int(input('Введите число'))
# i=2 #Простое число минимальное
# lst = []
# while i <= n:
#      if num % i == 0:
#         lst.append(i)

num = int(input("Введите число: "))
i = 2  # min простое число
lst = []
while i <= num:
    if num % i == 0: #остаток
        lst.append(i)
        num //= i
    else:
        i += 1
print(f"Простые множители числа приведены в списке: {lst}")