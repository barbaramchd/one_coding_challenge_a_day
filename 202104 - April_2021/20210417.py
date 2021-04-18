"""
Juraj loves donuts
"""
import random as rd


def simulate_donuts(n):
    available = [n]
    eaten = [0]
    spoiled = [0]
    half_life = 0

    while available[-1] > 0:
        eaten_today = 0
        spoiled_today = 0
        for donut in range(available[-1]):
            spoiled_cal = rd.random()
            eaten_cal = rd.random()
            if spoiled_cal <= 0.04:
                spoiled_today += 1
            elif eaten_cal <= 0.05:
                eaten_today += 1

        eaten.append(eaten[-1] + eaten_today)
        spoiled.append(spoiled[-1] + spoiled_today)
        available_today = available[-1] - (eaten_today + spoiled_today)
        available.append(available_today)

        if (eaten[-1] + spoiled[-1]) >= n / 2:
            if half_life == 0:
                half_life = len(eaten)

    return available, eaten, spoiled, half_life


donuts_simu = simulate_donuts(100)

import matplotlib.pyplot as plt

days = len(donuts_simu[0])
days_range = range(0, days)
plt.plot(days_range, donuts_simu[0], label = "Available")
plt.plot(days_range, donuts_simu[1], label = "Eaten")
plt.plot(days_range, donuts_simu[2], label = "Spoiled")
plt.ylabel('# of donuts')
plt.xlabel('Dasys')
plt.legend()
plt.show()