sample = [x.replace('\n', '') for x in open("input.txt").readlines()]


def path2COM(obj):
    path = []
    parent = orbits[obj]
    while parent != 'COM':
        parent = orbits[parent]
        path.append(parent)
    return path


orbits = {}
for orbit in sample:
    [orbited, orbiter] = orbit.split(")")
    orbits[orbiter] = orbited

pathYOU = path2COM('YOU')
pathSAN = path2COM('SAN')

for node in pathYOU:
    if node in pathSAN:
        ind1 = pathYOU.index(node) + 1
        ind2 = pathSAN.index(node) + 1
        break

print(ind1 + ind2)
