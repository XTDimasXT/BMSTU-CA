import newton
import util
import hermite


def system_solution(table_1, table_2, n):
    res_table = []
    for i in table_2:
        res_table.append([i[0], newton.interpolation(table_1, i[0], n) - i[1], i[2]])

    i = 0
    while i < len(res_table) - 1:
        if res_table[i + 1][1] > res_table[i][1]:
            res_table.pop(i)
        else:
            i += 1

    return newton.find_root(res_table, n)


def main():
    file_with_derivatives = open("der.txt", "r")
    file_table_1 = open("data1.txt", "r")
    file_table_2 = open("data2.txt", "r")
    table_with_derivatives = util.read_table(file_with_derivatives, 3)

    x = input('Введите х: ')
    try:
        x = float(x)
    except ValueError:
        print('Ошибка ввода')
        return

    if x < min([x[0] for x in table_with_derivatives]) or x > max([x[0] for x in table_with_derivatives]):
        print("Осторожно, будет выполняться экстраполяция!")

    print("Приблизительное значение:")
    print('-' * 64)
    print('|{:^20}|{:^20}|{:^20}|'.format('n', 'Newton', 'Hermite'))
    print('-' * 64)
    for i in range(1, len(table_with_derivatives)):
        print("|{:^20d}|{:^20.6f}|{:^20.6f}|".format(i, newton.interpolation(table_with_derivatives, x, i),
                                                     hermite.interpolation(table_with_derivatives, x, i)))
    print('-' * 64)

    print("Нахождение корня:")
    print('-' * 64)
    print('|{:^20}|{:^20}|{:^20}|'.format('n', 'Newton', 'Hermite'))
    print('-' * 64)
    for i in range(1, len(table_with_derivatives)):
        print("|{:^20d}|{:^20.6f}|{:^20.6f}|".format(i, newton.find_root(table_with_derivatives, i),
                                                     hermite.find_root(table_with_derivatives, i)))
    print('-' * 64)

    table_1 = util.read_table(file_table_1, 2)
    table_2 = util.read_table(file_table_2, 2)

    print("Решение системы:")
    print('-' * 43)
    print('|{:^20}|{:^20}|'.format('n', 'Root'))
    print('-' * 43)
    for i in range(1, 8):
        print("|{:^20d}|{:^20.6f}|".format(i, system_solution(table_1, table_2, i)))
    print('-' * 43)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

