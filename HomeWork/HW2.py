# #Задача 10:
#
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2
#
# headsTails = [1, 0, 1, 1, 0]
# heads = 0
# tails = 0
#
# for i in range(len(headsTails)):
#     if headsTails[i] == 1:
#         heads+=1
#     else:
#         tails+=1
# if heads > tails:
#     print(tails)
# else:
#     print(heads)
#

# #Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# s = int(input('Задай сумму двух чисел \n'))
# p = int(input('Задай произведение чисел \n'))
# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y:
#             print(f'первое число ="{x}", второе число ="{y}"')
#
# #Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
#

n = int(input('Введите число n: '))
k = 0
res = 1
while res < n+1:
    print(res)
    k += 1
    res = 2 ** k

