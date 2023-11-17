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
m = [5.9 * 10 ** 24, 7.34 * 10 ** 22]
init_a = [Vector(0, 0), Vector(0, 0)]
init_v = [[Vector(0, 0)], [Vector(0, 0)]]
init_x = [Vector(0, 0), Vector(384000000, 0)]
x = init_x

# creates pre-subtracted radii vectors
# list comprehension of radii to a body

radii = lambda _: [{k: v for sub_dict in sub_array for k, v in sub_dict.items()} for sub_array in
     [[{f"{i}{j}": (x[j] - x[i])} for j in range(len(x)) if x[i] != x[j]] for i in range(len(x))]]

r = radii("penis")

print(f"radii: {radii(1)}")

# list comprehension of forces of each body
forces = lambda _: [[G * m[i] * sum([m[j] * r[i][f'{i}{j}'] / r[i][f"{i}{j}"].length() ** 3]) for j in range(len(x)) if i != j] for i in range(len(x))]


f = forces("penis")

print(f"forces: {f}")

# list comprehension of accelerations
accs = lambda _: [[(f[i][j] / m[i]) for j in range(len(f[i]))] for i in range(len(f))]

a_prev = init_a
a = accs("penis")


print(f"accelerations: {a}")

# list comprehension of velocities
print(a_prev)
print(a)
vels = init_v
vels = lambda _: [[(0.5*(a_prev[i][j]+a[i][j]))*dt for j in range(len(f[i]))] for i in range(len(f))]

v = vels("penis")

print(f"velocities: {v}")

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
