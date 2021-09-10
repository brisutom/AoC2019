def calcFuel(mass):
    return mass//3 - 2


totFuel = 0
with open("input.txt") as f:
    for mass in f:
        fuel = calcFuel(int(mass))
    while fuel > 0:
        totFuel = totFuel + fuel
        fuel = calcFuel(fuel)


print(totFuel)
