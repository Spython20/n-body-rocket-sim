from vector import Vector
import numpy as np
from pprint import pprint
import time

start_time = time.time()

t = 0
i = 0
t_end = 100
dt = 0.001
G = 6.67430 * 10 ** -11

# initial conditions
m = [5.9 * 10 ** 24, 7.34 * 10 ** 22, 10]
init_a = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]
init_v = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]
init_x = [Vector(0, 0), Vector(384 * 10 ** 6, 0), Vector(20, 0)]

x = init_x
v = init_v
a = init_a

# creates pre-subtracted radii vectors
# list comprehension of radii to a body

calc_r = lambda _: [{k: v for sub_dict in sub_array for k, v in sub_dict.items()} for sub_array in
     [[{f"{i}{j}": (x[j] - x[i])} for j in range(len(x)) if i != j] for i in range(len(x))]]

r = calc_r('')

# list comprehension of forces of each body
calc_f = lambda _: [[G * m[i] * sum([m[j] * r[i][f'{i}{j}'] / r[i][f"{i}{j}"].length() ** 3]) for j in range(len(x)) if i != j] for i in range(len(x))]

f = calc_f('')

# Kinematics Section
# Acceletation
print(f'sum: {sum([Vector(0,0),Vector(0,0)])}')
# list comprehension of accelerations
calc_a = lambda _: [sum([(f[i][j] / m[i]) for j in range(len(f[i]))]) for i in range(len(f))]

a_prev = a
a = calc_a('')

# list comprehension of velocities
calc_v = lambda _: 1 / 2 * np.array([(np.array(a_prev[i])+np.array(a[i])) * dt for i in range(len(f))])

v_prev = v
v += calc_v('')
# list comprehension of positions
calc_x = lambda _: np.array([np.array(v_prev[i]) * dt + 1 / 2 * np.array(a_prev[i]) * dt ** 2 for i in range(len(f))])

x_prev = x
x += calc_x('')

pprint(f'r: {r}')
pprint(f'f: {f}')
pprint(f'a_prev: {a_prev}')
pprint(f'a: {a}')
pprint(f'v_prev: {v_prev}')
pprint(f'v: {v}')
pprint(f'x_prev: {x_prev}')
pprint(f'x: {x}')

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time)

'''
# THIS WORKS BUT I WANT SINGLE LINE LAMBDAS ONLY :))))))
def compute_accelerations(f):
    for i in range(len(f)):
        for j in range(len(f[i])):
            f[i][j] = (f[i][j] / m[i]) + init_a[i]

    return f

print(compute_accelerations(f))
'''


def update_positions(r, v, a, dt, i):
    pass


def update_velocities(v, a, dt, i):
    pass


def print_final_positions():
    pass


"""
while t < t_end:
    for body in a:
        a[body] = compute_accelerations(r, i)
    for body in r:
        r[body] = update_positions(r, v, a, dt, i)
    for body in a:
        a[body] = compute_accelerations(r, i)
    for body in v:
        v[body] = update_velocities(v, a, dt, i)
    t = t + dt
    # (print diagnostics here?)
print_final_positions()
"""
