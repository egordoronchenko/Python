# # HomeTask 24
# n = int(input("Введите кол-во кустов: "))
# count = [int(i) for i in input("Введите через пробел кол-во ягод на "
#                                "каждом кусте: ").split()[:n]]
# print(max([count[i - 2] + count[i - 1] + count[i] for i in range(n)]))


# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
# в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

#task 39
# N = int(input("Введите число элементов в 1м массиве"))
# list_1 = [int(i) for i in input("Введите через пробел значения: ").split()[:N]]
# M = int(input("Введите число элементов в 1м массиве"))
# list_2 = [int[i] for i in input("Введите значения через пробел для второго массива").split()[:M]]
#
# print(*[i for i in list_1 if i not in list_2])

# # Task 41
# n = int(input("Введите кол-во элементов списка: "))
# first_list = [int(i) for i in input("Введите значения списка: ").split()[:n]]
# # 12 35 8 9 1
# print(sum([first_list[i - 1] < first_list[i] > first_list[i + 1]
#            for i in range(1, n - 1)]))


# Task 43

# numbers = [int(i) for i in input("Введите числа: ").split()]
# count_numbers = {}
# for i in numbers:
#     if i not in count_numbers:  # count_numbers.keys()
#         count_numbers[i] = 1  # 1 - потому что одно число уже нам встретилось
#     else:  # i является ключом словаря
#         count_numbers[i] += 1
# print(count_numbers)
# print(sum([i // 2 for i in count_numbers.values()]))


#task 45
n = int(input("Input number: "))
data = {}
for i in range(2, n + 1):
    summa = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            summa += j
    data[i] = summa
print_list = list()
for k, v in data.items():
    if v in data.keys() and k in data.values() and k != v and data[v] == k and data[k] == v\
            and (k, v) not in print_list:
        print(k, v)
        print_list.append((v, k))