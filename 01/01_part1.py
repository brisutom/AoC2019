import math

fuel = 0
with open("input.txt") as f:
    for mass in f:
        fuel = fuel + math.floor((int(mass)/3))-2

print(fuel)
