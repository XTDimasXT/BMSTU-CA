import sympy as sym
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.linalg import solve

N = 3
eps = 1e-3

def Newton(F, Jacobian):
    curValues = np.array([0.5, 0.5, 0.5], dtype="float")

    FCur = F(*curValues)
    JacobianCur = Jacobian(*curValues)

    delta = solve(JacobianCur, FCur).reshape((N, ))
    curValues += delta
    
    while np.linalg.norm(delta) > eps:
        
        curValues -= delta

        FCur = F(*curValues)
        JacobianCur = Jacobian(*curValues)

        delta = solve(JacobianCur, FCur).reshape((N, ))

    return curValues


def Newton_3rd(F, Jacobian, initValues):
    curValues = np.array(initValues, dtype="float")

    FCur = F(*curValues)
    JacobianCur = Jacobian(*curValues)

    delta = solve(JacobianCur, FCur).reshape((N + 1, ))
    curValues += delta

    while np.linalg.norm(delta) > eps:
        
        curValues -= delta

        FCur = F(*curValues)
        JacobianCur = Jacobian(*curValues)

        delta = solve(JacobianCur, FCur).reshape((N + 1, ))

    return curValues


def f(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)


def simpson(xCur):
    steps = 200
    step = xCur / (steps * 2)

    xValues = np.array([i * step for i in range(steps * 2 + 1)])
    funcValues = np.array([f(x_i) for x_i in xValues])

    sumX1 = 4 * np.sum([funcValues[2 * i - 1] for i in range(1, steps)])
    sumX2 = 2 * np.sum([funcValues[2 * i] for i in range(1, steps - 1)])

    return (step / 3) * (funcValues[0] + funcValues[-1] + sumX1 + sumX2)


vars = ['x', 'y', 'z']
funcs = ['x ** 2 + y ** 2 + z ** 2 - 1',
         '2 * x ** 2 + y ** 2 - 4 * z',
         '3 * x ** 2 - 4 * y + z ** 2']

F = sym.Matrix(funcs)
Jacobian = sym.Matrix(funcs).jacobian(vars)

Jacobian = sym.lambdify(sym.symbols(vars), Jacobian)
F = sym.lambdify(sym.symbols(vars), F)

values = Newton(F, Jacobian)
space = ' '

print("=====TASK #1=====")
print(f"x: {values[0]:.5f}\ny: {values[1]:.5f}\nz: {values[2]:.5f}\n")

print("=====TASK #2=====")
ans = simpson(values[0])
print(f"{ans:.5f}")

N = 100
eps = 1e-3

start = [0, 1]
end = [1, 3]

step = (end[0] - start[0]) / N
xValues = np.array([i * step for i in range(N + 1)])

vars = [f'y{i}' for i in range(N + 1)]

funcs = [f'{vars[i - 1]} - 2 * {vars[i]} + {vars[i + 1]} - ({step} ** 2) * ({vars[i]} ** 3 + {xValues[i]} ** 2)' for i in range(1, N)]
funcs.extend(['y0 - 1', f'y{N} - 3'])

F = sym.Matrix(funcs)
Jacobian = sym.Matrix(funcs).jacobian(vars)

Jacobian = sym.lambdify(sym.symbols(vars), Jacobian)
F = sym.lambdify(sym.symbols(vars), F)

delta = (end[1] - start[1]) / (end[0] - start[0])
initValues = [start[1] + delta * i * step for i in range(N + 1)]

yValues = Newton_3rd(F, Jacobian, initValues)

plt.grid()
plt.plot(xValues, initValues, label = "Init values")
plt.plot(xValues, yValues, label = "Result values")
plt.legend()
plt.show()
    
print(yValues[30:40])