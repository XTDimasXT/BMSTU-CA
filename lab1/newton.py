def calc_coeffs(table):
    temp = [[0] * (len(table)) for i in range(len(table) + 2)]
    for i in range(len(table)):
        temp[0][i] = table[i][0]
        temp[1][i] = table[i][2]
        temp[2][i] = table[i][1]

    x_barier = 1

    for i in range(3, len(temp)):
        for j in range(len(temp[0]) - i + 2):
            if abs(temp[0][j] - temp[0][j + x_barier]) < 1e-6:
                temp[i][j] = temp[1][j]
            else:
                temp[i][j] = (temp[i - 1][j] - temp[i - 1][j + 1]) / (temp[0][j] - temp[0][j + x_barier])
        x_barier += 1

    return [temp[i][0] for i in range(3, len(temp))]


def select_points(table, x, n) -> list[list[float]]:
    new_table = []

    pos = 0
    # находим первую точку которая больше х
    while pos < len(table) - 1 and table[pos][0] < x:
        pos += 1

    # выбираем наиболее близку к х точку (это или pos или pos - 1)
    if pos != 0 and abs(table[pos][0] - x) > abs(table[pos - 1][0] - x):
        pos -= 1

    new_table.append(table[pos].copy())

    l_bound = pos - 1
    r_bound = pos + 1

    # print(len(table), n)

    # Расходимся в обе стороны
    while len(new_table) < n + 1:
        if l_bound >= 0 and len(new_table) < n + 1:
            new_table.append(table[l_bound].copy())
            l_bound -= 1
        if r_bound < len(table) and len(new_table) < n + 1:
            new_table.append(table[r_bound].copy())
            r_bound += 1

    # Восстанавливаем порядок
    new_table.sort(key=lambda x: x[0])

    assert len(new_table) == n + 1
    return new_table


def interpolation(table, x, n):
    selected_points = select_points(table, x, n)
    coeffs = calc_coeffs(selected_points)

    return calc_polynom(selected_points, coeffs, x)


def calc_polynom(points, coeffs, x):
    res = points[0][1]
    accum = 1
    i = 0
    while i < len(coeffs):
        accum *= (x - points[i][0])
        res += accum * coeffs[i]
        i += 1

    return res


def find_root(table, n):
    inverse_table = []

    for i in range(len(table)):
        inverse_table.append([table[i][1], table[i][0], 1 / table[i][2]])

    inverse_table.sort(key=lambda x: x[0])

    return interpolation(inverse_table, 0, n)
