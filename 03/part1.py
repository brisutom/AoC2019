input1 = open("input.txt").readlines()[0].split(",")
input1[-1] = input1[-1].replace("\n", "")
input2 = open("input.txt").readlines()[1].split(",")


def splitInput(inputInstr):
    result = []
    for instruction in inputInstr:
        result.append((instruction[0], int(instruction[1:])))
    return result


def addPoints(a, b):
    return tuple(map(lambda x, y: x+y, a, b))


def getPoints(route):
    points = []
    point = (0, 0)
    for (direction, dist) in route:
        if direction == "R":
            new_points = list(map((lambda new: addPoints(point, new)), [(x, 0) for x in range(dist+1)]))
        elif direction == "L":
            new_points = list(map((lambda new: addPoints(point, new)), [(-x, 0) for x in range(dist+1)]))
        elif direction == "U":
            new_points = list(map((lambda new: addPoints(point, new)), [(0, y) for y in range(dist+1)]))
        elif direction == "D":
            new_points = list(map((lambda new: addPoints(point, new)), [(0, -y) for y in range(dist+1)]))

        point = new_points[-1]
        points = points + new_points

    return points


def manhattan(point):
    return abs(point[0]) + abs(point[1])


points1 = getPoints(splitInput(input1))
points2 = getPoints(splitInput(input2))

intersections = list(set(points1) & set(points2))
intersections.remove((0, 0))
print(min(list(map(manhattan, intersections))))
