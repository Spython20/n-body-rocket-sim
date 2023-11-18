from vector import Vector
from planet import Planet
import numpy as np
from pprint import pprint
import time
import pygame

start_time = time.time()

t = 0
i = 0
t_end = 100
dt = 0.01
G = 6.67430 * 10 ** -11

# initial conditions
m = [5.9 * 10 ** 24, 7.34 * 10 ** 22, 10]
init_a = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]
init_v = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]
init_x = [Vector(0, 0), Vector(384 * 10 ** 6, 0), Vector(20, 0)]
r_body = [8, 8, 8]

data = []

x = init_x
v = init_v
a = init_a

for t in np.arange(0, t_end, dt):
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
    # list comprehension of accelerations
    calc_a = lambda _: [sum([(f[i][j] / m[i]) for j in range(len(f[i]))]) for i in range(len(f))]

    a_prev = a
    a = calc_a('')

    # list comprehension of velocities
    calc_v = lambda _: (1 / 2) * np.array([(np.array(a_prev[i])+np.array(a[i])) * dt for i in range(len(f))])

    v_prev = v
    v += calc_v('')
    # list comprehension of positions
    calc_x = lambda _: np.array([np.array(v_prev[i]) * dt + 1 / 2 * np.array(a_prev[i]) * dt ** 2 for i in range(len(f))])

    x_prev = x
    x += calc_x('')
    data.append( {
        't': t,
        'x': x,
        'v': v,
        'a': a,
        'f': f,
        'r': r
    })

pprint(data[0]['x'][0])
end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time)

"""
THIS IS WHERE THE ANIMATION BEGINS
"""

screen = pygame.display.set_mode((960, 720))
planets = []

for i in range(len(m)):
    planets.append(Planet(init_x[i], r_body[i]))


print(planets)
pygame.init()

app_running = True

def draw():
    screen.fill((50, 50, 50))

#def update():


while app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False


    draw()

    #update()

    pygame.display.flip()

pygame.quit()
