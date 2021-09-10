sample = [x[:-1] for x in open("input.txt").readlines()]


def short2COM(obj):
    if obj == 'COM':
        return 0
    result = 1
    parent = orbits[obj]
    while parent != 'COM':
        result = result + 1
        parent = orbits[parent]
    return result


orbits = {}
for orbit in sample:
    [orbited, orbiter] = orbit.split(")")
    orbits[orbiter] = orbited

objects = set(orbits.keys()).union(set(orbits.values()))

print(sum(map(short2COM, objects)))
