from vector import Vector
from planet import Planet
import numpy as np
from pprint import pprint
import time
import pygame
import copy

start_time = time.time()

t_end = 100
dt = 0.01
time_index = 0
G = 10 #6.67430 * 10 ** -11

# initial conditions
m = [20, 300, 100, 20, 300, 100]
init_a = [Vector(0, 0), Vector(0, 0), Vector(0, 0), Vector(0, 0), Vector(0, 0), Vector(0, 0)]
init_v = [Vector(10, 10), Vector(10, 0), Vector(0, 0), Vector(10, 10), Vector(10, 0), Vector(0, 0)]
init_x = [Vector(100, 200), Vector(200, 300), Vector(300, 400), Vector(50, 200), Vector(100, 300), Vector(500, 400)]
r_body = [8, 8, 8, 8, 8, 8]

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

    a_prev = copy.deepcopy(a)
    a = calc_a('')

    # list comprehension of velocities
    calc_v = lambda _: 1 / 2 * np.array([(np.array(a_prev[i])+np.array(a[i])) * dt for i in range(len(f))])

    v_prev = copy.deepcopy(v)
    v += calc_v('')
    # list comprehension of positions
    calc_x = lambda _: np.array([np.array(v_prev[i]) * dt + 1 / 2 * np.array(a_prev[i]) * dt ** 2 for i in range(len(f))])

    x_prev = copy.deepcopy(x)
    x += calc_x('')
    data.append({
        't': t,
        'x': copy.deepcopy(x),
        'v': copy.deepcopy(v),
        'a': copy.deepcopy(a),
        'f': copy.deepcopy(f)
    })


end_time = time.time()
execution_time = end_time - start_time

#for i in range(len(data)): 
  # pprint(data[i]['x'])

print("Execution time:", execution_time)

"""
THIS IS WHERE THE ANIMATION BEGINS
"""

screen = pygame.display.set_mode((960, 720))
planets = []

for i in range(len(m)):
    planets.append(Planet(init_x[i], r_body[i]))

pygame.init()

clock = pygame.time.Clock()
app_running = True

def draw():
    screen.fill((50, 50, 50))
    for planet in planets:
        planet.draw(screen)

def timer_tick():
    global time_index
    time_index += 1

def update_all_planets(animation_time):
    
    print(animation_time)
    for i in range(len(planets)):\
        planets[i].update(data, i, animation_time)

        #print(f"planet {i}: " + str(planets[i].position))


while app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False


    draw()

    delta_time = dt * clock.tick(144)
    timer_tick()
    update_all_planets(time_index)

    pygame.display.flip()

pygame.quit()
