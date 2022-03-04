def delete_cr(massive: list, x: int, y: int):
    '''вариант реализация без рекурсии'''
    qu_v = []
    qu_v.append((x, y))
    while(len(qu_v) > 0):
        t = qu_v.pop(0)
        while massive[t[0]][t[1]] == '1':
            massive[t[0]][t[1]] = 0
            if (t[0] - 1) >= 0 and (t[0] - 1) < len(massive):
                qu_v.append((t[0] - 1, t[1]))
            if (t[0] + 1) >= 0 and (t[0] + 1) < len(massive):
                qu_v.append((t[0] + 1, t[1]))
            if (t[1] - 1) >= 0 and (t[1] - 1) < len(massive):
                qu_v.append((t[0], t[1] - 1))
            if (t[1] + 1) >= 0 and (t[1] + 1) < len(massive):
                qu_v.append((t[0], t[1] + 1))
        massive[t[0]][t[1]] = 0


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
                delete_cr(lst, i_mas, index_i)
                cr_count += 1
    return print(int(cr_count))


calculate()
