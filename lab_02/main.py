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

new_x = np.linspace(min(x) - 0.5, max(x) + 0.5, 150)

print_table(table, x_single, spline_natural, spline_left_edge_newton, spline_both_edge_newton)

fig, ax = plt.subplots()
plt.title("Интерполяция с помощью кубических сплайнов")
ax.plot(x, y, label='Изначальная таблица')
ax.plot(new_x, [spline_natural.aproximate_value(i) for i in new_x], label='Сплайн (0, 0)')
ax.plot(new_x, [spline_left_edge_newton.aproximate_value(i) for i in new_x], label='Сплайн (P``(x0), 0)')
ax.plot(new_x, [spline_both_edge_newton.aproximate_value(i) for i in new_x], label='Сплайн (P``(x0), P``(xn))')
ax.plot(new_x, [approximate_newton(table, i, 3) for i in new_x], label='Полином Ньютона 3-ей степени')

ax.legend()
ax.grid() 

plt.show()