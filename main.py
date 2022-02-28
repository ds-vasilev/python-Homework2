from typing import Any


def records_find(i_mas: int, index_i: int, massive: Any) -> None:
    '''
    Проверяет вхождение подаваемого индекса в массив, находит первую единицу,
    после чего рекурсивно вызывает себя для соседних ячеек.
    '''
    if i_mas >= 0 and i_mas < len(massive) and index_i >= 0 and index_i < len(massive[0]):
        if massive[i_mas][index_i] == '1':
            massive[i_mas][index_i] = 0
            records_find(i_mas - 1, index_i, massive)
            records_find(i_mas + 1, index_i, massive)
            records_find(i_mas, index_i - 1, massive)
            records_find(i_mas, index_i + 1, massive)


def calculate() -> None:
    '''
    Получаем данные из файла как  двумерный массив, при нахождении единицы
    вызывает рекурсивную функцию, по выходу из рекурсии добавляет в счетчик +1.
    '''
    with open('src.txt', 'r') as file:
        lst = file.readlines()
    lst = [[str(n) for n in x.split()] for x in lst]
    cr_count = 0
    for i_mas, val_mas in enumerate(lst):
        for index_i, val_i in enumerate(val_mas):
            if val_i == '1':
                records_find(i_mas, index_i, lst)
                cr_count += 1
    return print(int(cr_count))


calculate()
