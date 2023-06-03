import pandas as pd

x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

# 1
def get_left_derivative(y0, y1, h=1):
    return (y1 - y0) / h

one = [get_left_derivative(y[i], y[i + 1]) for i in range(len(y) - 1)] + [None]

# 2
def get_center_derivative(y0, y2, h=1):
    return (y2 - y0) / (2*h)

two = [None] + [get_center_derivative(y[i - 1], y[i + 1]) for i in range(1, len(y) - 1)] + [None]

# 3
def get_second_runge_formula_derivative(y0, y1, y2):
    d1 = get_left_derivative(y0, y1, 1)
    d2 = get_left_derivative(y0, y2, 2)
    
    return d1 + (d1 - d2) / 3

three = [None] + [get_second_runge_formula_derivative(y[i - 1], y[i], y[i + 1]) for i in range(1, len(y) - 1)] + [None]

# 4
def get_alignment_variables_derivative(y0, y1, x0, x1):
    eta0 = 1/y0
    eta1 = 1/y1
    
    ksi0 = 1/x0
    ksi1 = 1/x1
    
    a1 = eta1 - eta0
    a0 = ksi1 - ksi0
    
    derivative = (a1 / a0) * (y0 ** 2) / (x0 ** 2) # der. in (x0, y0)
    
    return derivative
    
four = [get_alignment_variables_derivative(y[i], y[i+1], x[i], x[i+1]) for i in range(len(y) - 1)] + [None]

# 5
def get_second_derivative(y0, y1, y2, h=1):
    return (y0 - 2 * y1 + y2) / (h ** 2)

five = [None] + [get_second_derivative(y[i - 1], y[i], y[i + 1]) for i in range(1, len(y) - 1)] + [None]

dickt = {
    'X': x,
    'Y': y,
    '1 (Left)': one,
    '2 (Center)': two,
    '3 (Runge)': three,
    '4 (Align. vars)': four,
    '5 (Second der.)': five
}

df = pd.DataFrame(dickt).reset_index(drop=True)

print(df)