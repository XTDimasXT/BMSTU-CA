def file_read(file_name):
    try:
        f = open(file_name, "r")
        table = [list(map(float, string.split())) for string in list(f)]
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
            ##print("%12f" %(table[i][j]), end = '')
        print()

    print("|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 11 + "|")
    print()


def read_degree_and_value(length):
    try:
        n = int(input("Введите степень аппроксимирующего полинома:"))
        if (n <= 0 or n >= length):
            print("Степень должна находиться в диапазоне от 1 до {}".format(length - 1))
            return -1, -1
        
        x = float(input("Введите значение аргумента, для которого выполняется интерполяция:"))
        return n, x
    except:
        print("Некорректный ввод данных")
        return -1, -1


def main():
    file_name = str(input("Введите название файла: "))

    table = file_read(file_name)
    if len(table) == 0:
        return
    
    table.sort(key = lambda arr: arr[0])
    print_table(table)

    length = len(table)
    n, x = read_degree_and_value(length)
    if n == -1:
        return
    


if __name__ == "__main__":
    main()