from return_data_file import data_file
from print_data import print_file



def copy_data():
    print()
    print()
    print("Сейчас выберем c какого файла будем копировать")
    data1, nf1 = data_file()
    count_rows1 = len(data1)

    print()
    print()
    print("А сейчас выберем в какой файл будем добавлять")
    data2, nf2 = data_file()
    count_rows2 = len(data2)

    all = "ВСЕ"
    if count_rows1 == 0:
        print("Файл пусто!")
    else:
        number_row = input(f'Введите номер строки '
                           f'от 1 до {count_rows1}, если требуется скопировать все строки "Все": ')

        if number_row.upper() == all:
            count = 1
            for i in data1:
                stroka = i.split(';')
                with open(f'db/data_{nf2}.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{count_rows2 + count};{stroka[1]};'
                               f'{stroka[2]};{stroka[3]};{stroka[4]}')
                count = count + 1
            print("Данные успешно записаны!")
            print()


        else:
            number_row = int(number_row)
            while number_row < 1 or number_row > count_rows1:
                number_row = int(input(f"Ошибка!"
                                       f"Введите номер строки "
                                       f"от 1 до {count_rows1}: "))

            stroka = data1[number_row-1].split(';')

            with open(f'db/data_{nf2}.txt', 'a', encoding='utf-8') as file:
                file.write(f'{count_rows2+1};{stroka[1]};'
                           f'{stroka[2]};{stroka[3]};{stroka[4]}')
            print("Данные успешно записаны!")
            print()




