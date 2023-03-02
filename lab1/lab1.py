def file_read(file_name):
    try:
        f = open(file_name, "r")
        table = [list(map(float, string.split())) for string in list(f)]
        print(table)
        return table
    except:
        print("Файл не найден")
        return []


def print_table(table):
    print("|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 11 + "|")
    print("|{:^11}|{:^11}|{:^11}|".format("x", "y", "y'"))
    print("|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 11 + "|")

    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == 0:
                print("|{:^11}|".format(table[i][j]), end = '')
            else:
                print("{:^11}|".format(table[i][j]), end = '')
        print()
        print("|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 11 + "|")

    print()


def read_degree_and_value(length):
    try:
        n = int(input("Введите степень аппроксимирующего полинома: "))
        if (n <= 0 or n >= length):
            print("Степень должна находиться в диапазоне от 1 до {}".format(length - 1))
            return -1, -1
        
        x = float(input("Введите значение аргумента, для которого выполняется интерполяция: "))
        return n, x
    except:
        print("Некорректный ввод данных")
        return -1, -1

    
def create_table_x_y(table):
    table_x_y = []

    temp = []
    for i in range(len(table)):
        temp.append(table[i][0])
    table_x_y.append(temp)

    temp = []
    for i in range(len(table)):
        temp.append(table[i][1]) 
    table_x_y.append(temp)

    return table_x_y


def divided_differences(table, rank):
    if rank <= len(table) - 2:
        return table

    rank -= (len(table) - 2)
    for i in range(len(table), len(table) + rank):
        table.append([])
        for j in range(len(table[i - 1]) - 1):
            table[i].append((table[i - 1][j] - table[i - 1][j + 1]) / (table[0][j] - table[0][j + i - 1]))

    return table


def print_row_sep(col_n, col_size):
    for i in range(col_n):
        print("|" + "-" * col_size, end='')
    print("|")


def print_table_new(table, col_size):
    print()
    print_row_sep(len(table), col_size)

    print("|{0:^{2}}|{1:^{2}}".format("x", "y", col_size), end='')
    for i in range(len(table) - 2):
        print("|{0:^{1}}".format("y" + '\'' * (i + 1), col_size), end='')
    print('|')

    print_row_sep(len(table), col_size)

    for j in range(len(table[0])):
        for i in range(len(table)):
            if j < len(table[i]):
                print("|{0:^{1}.6f}".format(table[i][j], col_size), end='')
            else:
                print("|{0:^{1}}".format('-', col_size), end='')
        print("|")

        print_row_sep(len(table), col_size)
    print()


def find_index(table, x, n):
    diff = abs(table[0][0] - x)
    index = 0
    for i in range(1, len(table[0]) - n):
        if abs(table[0][i] - x) < diff:
            index = i
            diff = abs(table[0][i] - x)

    return index


def newton_polynomial(table, n, x, index):
    result = table[1][index]
    for i in range(2, n + 2):
        temp_res = 1
        for j in range(i - 1):
            temp_res *= x - table[0][j + index]
        temp_res *= table[i][index]
        result += temp_res

    return result


def hermit_polynomial():
    return 1


def perform_first_task(table, x):
    result_newton = []
    for i in range(1, 6):
        index = find_index(table, x, i)
        newton_pol = newton_polynomial(table, i, x, index)
        result_newton.append(newton_pol)
    
    return result_newton


def print_table_first_task(result_newton, col_size):
    print_row_sep(len(result_newton) + 1, col_size)
    print("|{0:^{6}}|{1:^{6}}|{2:^{6}}|{3:^{6}}|{4:^{6}}|{5:^{6}}|".format("N", "1", "2", "3", "4", "5", col_size))
    print_row_sep(len(result_newton) + 1, col_size)

    print("|  Newton   ", end='')
    for i in range(len(result_newton)):
        print("|{0:^{1}.6f}".format(result_newton[i], col_size), end='')
    print("|", end='')
    print()

    print_row_sep(len(result_newton) + 1, col_size)

    print("|  Hermit   ", end='')
    for i in range(len(result_newton)):
        print("|{0:^{1}.6f}".format(result_newton[i], col_size), end='')
    print("|", end='')
    print()

    print_row_sep(len(result_newton) + 1, col_size)


def main():
    file_name = str(input("Введите название файла: "))
    print(file_name)

    table = file_read(file_name)
    if len(table) == 0:
        return
    
    table.sort(key = lambda arr: arr[0])
    print_table(table)

    length = len(table)
    n, x = read_degree_and_value(length)
    if n == -1:
        return

    table_x_y = create_table_x_y(table)
    table_x_y = divided_differences(table_x_y, n)
    print_table_new(table_x_y, 11)

    index = find_index(table_x_y, x, n)
    newton_pol = newton_polynomial(table_x_y, n, x, index)
    print("Newton = {:.6f}".format(newton_pol))
    print()

    table_x_y = create_table_x_y(table)
    table_x_y = divided_differences(table_x_y, 5)

    result_newton = perform_first_task(table_x_y, x)
    print_table_first_task(result_newton, 11)

    # print("Hermit = %.6f".format(hermit_pol))
    # print("Root = %.6f".format(root))


if __name__ == "__main__":
    main()