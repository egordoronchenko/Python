# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
#
# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list2 = set()
# for i in list1:
#     list2.add(i)
#
# print(len(list2))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально

# initialList = [1, 2, 3, 4, 5]
# k = 3
# resultlist = []
# resultlist = initialList[k:] + initialList[:k]
# print(resultlist)

# Напишите программу для печати всех уникальных
# значений в словаре.
# list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list1 = [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"},
         {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ": " S009 "},
         {" VIII ": " S007 ", "XII": "D001"}]
# Создаем множество.
# затем перебирая сначала значения в листе
# получаем значение в каждом словаре добавляя его в множество.
# если значение повторяется оно по правилу множества не добавляется

# result = set()
# for item in list1:
#     for key, value in item.items():
#         result.add(value.strip())
# print (result)
#
result = {value.strip() for item in list1 for key, value in item.items()}

print(result)
