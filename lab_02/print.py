from spline import *
from newton import *

def print_table(table, x_single, spline_natural, spline_left_edge_newton, spline_both_edge_newton):
    str_spline_natural = "Сплайн с натуральными краевыми условиями"
    str_spline_left = "Сплайн с краевыми условиями P''(x0) и 0"
    str_spline_both = "Сплайн с краевыми условиями P''(x0) и P''(xn)"
    str_polynomial_newton = "Полином Ньютона 3-ей степени"

    print("")
    print("=" * 24 + "ИТОГОВЫЕ РАСЧЕТЫ" + "=" * 24)
    print("Выбранная точка: x = {0}".format(x_single))
    print("-" * 64)
    print('|{:^50}|{:^11.3f}|'.format(str_spline_natural, spline_natural.aproximate_value(x_single)))
    print("-" * 64)
    print('|{:^50}|{:^11.3f}|'.format(str_spline_left, spline_left_edge_newton.aproximate_value(x_single)))
    print("-" * 64)
    print('|{:^50}|{:^11.3f}|'.format(str_spline_both, spline_both_edge_newton.aproximate_value(x_single)))
    print("-" * 64)
    print('|{:^50}|{:^11.3f}|'.format(str_polynomial_newton, approximate_newton(table, x_single, 3)))
    print("=" * 64)