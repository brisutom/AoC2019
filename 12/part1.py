import itertools


class Moon:
    def __init__(self, pos_init, label=None, vel_init=None):
        if vel_init is None:
            self.vx = 0
            self.vy = 0
            self.vz = 0
        else:
            self.vx = vel_init[0]
            self.vy = vel_init[1]
            self.vz = vel_init[2]

        self.x = pos_init[0]
        self.y = pos_init[1]
        self.z = pos_init[2]
        self.label = label

    def __str__(self):
        return self.label

    def print_state(self):
        print("x: " + str(self.x) + ", y: " + str(self.y) + ", z: " +
              str(self.z) + "; vx: " + str(self.vx)
              + ", vy: " + str(self.vy) + ", vz: " + str(self.vz))

    @property
    def pot(self):
        return sum(map(abs, [self.x, self.y, self.z]))

    @property
    def kin(self):
        return sum(map(abs, [self.vx, self.vy, self.vz]))


io = Moon([-17, 9, -5], "io")
eu = Moon([-1, 7, 13], "eu")
gan = Moon([-19, 12, 5], "gan")
cal = Moon([-6, -6, -4], "cal")

moons = [io, eu, gan, cal]

steps = 1000
for t in range(steps):
    # for moon in moons:
    #     moon.print_state()
    # print("_" * 30)
    combs = itertools.combinations(moons, 2)
    for moon1, moon2 in combs:
        if moon1.x < moon2.x:
            moon1.vx = moon1.vx + 1
            moon2.vx = moon2.vx - 1
        elif moon1.x > moon2.x:
            moon1.vx = moon1.vx - 1
            moon2.vx = moon2.vx + 1

        if moon1.y < moon2.y:
            moon1.vy = moon1.vy + 1
            moon2.vy = moon2.vy - 1
        elif moon1.y > moon2.y:
            moon1.vy = moon1.vy - 1
            moon2.vy = moon2.vy + 1

        if moon1.z < moon2.z:
            moon1.vz = moon1.vz + 1
            moon2.vz = moon2.vz - 1
        elif moon1.z > moon2.z:
            moon1.vz = moon1.vz - 1
            moon2.vz = moon2.vz + 1

    for moon in moons:
        moon.x = moon.x + moon.vx
        moon.y = moon.y + moon.vy
        moon.z = moon.z + moon.vz

print(sum([(x.pot * x.kin) for x in moons]))
