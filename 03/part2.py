input1 = open("input.txt").readlines()[0].split(",")
input1[-1] = input1[-1].replace("\n", "")
input2 = open("input.txt").readlines()[1].split(",")


def splitInput(inputInstr):
    result = []
    for instruction in inputInstr:
        result.append((instruction[0], int(instruction[1:])))
    return result


def addPoints(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def getPoints(route):
    points = []
    point = [0, 0, 0]
    for (direction, dist) in route:
        if direction == "R":
            new_points = list(map((lambda new: addPoints(point, new)), [[x, 0, x] for x in range(dist+1)]))
        elif direction == "L":
            new_points = list(map((lambda new: addPoints(point, new)), [[-x, 0, x] for x in range(dist+1)]))
        elif direction == "U":
            new_points = list(map((lambda new: addPoints(point, new)), [[0, y, y] for y in range(dist+1)]))
        elif direction == "D":
            new_points = list(map((lambda new: addPoints(point, new)), [[0, -y, y] for y in range(dist+1)]))

        point = new_points[-1]
        points = points + new_points

    return points


def delayDist(point):
    return abs(point[3])


points1 = getPoints(splitInput(input1))
points2 = getPoints(splitInput(input2))

# this takes forever, turns out the set functions in python I used in part1 are really fast
intersections = []
for a in points1:
    for b in points2:
        if a[0] == b[0] and a[1] == b[1]:
            intersections.append([a, a[2] + b[2]])

delays = []
for a in intersections:
    if a[1] != 0:
        delays.append(a[1])

print(min(delays))
