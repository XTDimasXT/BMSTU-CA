import sys


def read_table(file, fields_num) -> list[list[float]]:
    table = []
    for line in file:
        try:
            table_row = list(map(float, line.split()))
            assert len(table_row) == fields_num
            if fields_num == 2:
                table_row.append(1)
            table.append(table_row)
        except ValueError:
            print("Неверные данные для прочтения")
            raise Exception
        except AssertionError:
            print("Кол-во столбцов отличается от заданного")
            raise Exception
    return table

