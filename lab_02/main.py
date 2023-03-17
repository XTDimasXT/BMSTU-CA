import matplotlib.pyplot as plt
import numpy as np

from spline import *
from newton import *
from file import *
from print import *

file_name = input("Введите название файла: ")
table = read_file(file_name)
x_single = float(input('Введите х: '))

x = [x[0] for x in table]
y = [y[1] for y in table]

selected_points_left = select_points_newton(table, min(x), 3)
selected_points_right = select_points_newton(table, max(x), 3)

divided_diffs_left = divided_diff(selected_points_left)
divided_diffs_right = divided_diff(selected_points_right)

newton_sec_dir_left = divided_diffs_left[1] + divided_diffs_left[2] * (4 * min(x) - 2 * selected_points_left[2][0])
newton_sec_dir_right = divided_diffs_right[1] + divided_diffs_right[2] * (4 * max(x) - 2 * selected_points_right[2][0])

spline_natural = Spline(table, 0, 0)
spline_left_edge_newton = Spline(table, newton_sec_dir_left, 0)
spline_both_edge_newton = Spline(table, newton_sec_dir_left, newton_sec_dir_right)

print_table(table, x_single, spline_natural, spline_left_edge_newton, spline_both_edge_newton)