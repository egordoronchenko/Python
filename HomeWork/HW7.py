# def rhythm(poem):
#     poem = poem.split()
#     f = lambda word: sum(1 for i in word if i in 'аеёиоуыэюя')
#     sum_word = f(poem[0])
#     return all([f(i) == sum_word for i in poem])
#
# poem = str(input("Введите стихотворение: "))
#
# if rhythm(poem):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

def print_operation_table(operation, num_rows=6, num_columns=8):
    res = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in res:
        print(*[f"{j}" for j in i])

print_operation_table(lambda x, y: x * y)