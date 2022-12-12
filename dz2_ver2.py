# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# старое решение

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list2 = [] 
# for i in list:
#     y = str(i)
#     list2.append(y)
# print(list2)
# list3 = []
# for i in list2:
#     if ("." in i):
#         x = i.split(".")
#         y = "0."
#         y = y+x[1]
#         list3.append(float(y))
# Max = list3[0]
# min = list3[0]
# for i in list3:
#     if (i > Max):
#         Max = i
# print(f'Максимальная дробная часть= {Max}')
# for i in list3:
#     if (i < min):
#         min = i
# print(f'Минимальная дробная часть= {min}')
# print(f'Max-Min = {Max-min}')

# новое решение

list = [1.1, 1.2, 3.1, 5, 10.01]
list = [str(i) for i in list]
print(list)
list = [i.split(".") for i in list if '.'in i]
list = [float('0.' + i[1]) for i in list]
print(lis t)
print(max(list)-min(list))
