import newton


def select_points(table, x, n):
    new_table = []
    pos = 0
    while pos < len(table) - 1 and table[pos][0] < x:
        pos += 1
    if pos != 0 and abs(table[pos][0] - x) > abs(table[pos - 1][0] - x):
        pos -= 1
    new_table.append(table[pos].copy())
    if len(new_table) < n + 1:
        new_table.append(table[pos].copy())

    l_bound = pos - 1
    r_bound = pos + 1

    while len(new_table) < n + 1:
        if l_bound >= 0 and len(new_table) < n + 1:
            new_table.append(table[l_bound].copy())
            if len(new_table) < n + 1:
                new_table.append(table[l_bound].copy())
            l_bound -= 1
        if r_bound < len(table) and len(new_table) < n + 1:
            new_table.append(table[r_bound].copy())
            if len(new_table) < n + 1:
                new_table.append(table[r_bound].copy())
            r_bound += 1

    new_table.sort(key=lambda x: x[0])

    assert len(new_table) == n + 1
    return new_table


def interpolation(table, x, n):
    selected_points = select_points(table, x, n)
    coeffs = newton.calc_coeffs(selected_points)

    return newton.calc_polynom(selected_points, coeffs, x)


def find_root(table, n):
    inverse_table = []

    for i in range(len(table)):
        inverse_table.append([table[i][1], table[i][0], 1 / table[i][2]])

    inverse_table.sort(key=lambda x: x[0])

    return interpolation(inverse_table, 0, n)
