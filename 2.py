import time

horizontal = 0
depth = 0
aim = 0

f = open("input2.txt", "r")

list = []

for x in f.read().split("\n"):
    list.append(x.split(" "))

dir = ""
am = 0
for x in list:
    #time.sleep(0.01)

    dir = x[0]
    am = int(x[1])
    if (dir == "forward"):
        horizontal = horizontal + am
        depth = depth + (aim*am)
    elif (dir == "down"):
        aim = aim + am
        #depth = depth + am
    else:
        aim = aim - am
        #depth = depth - am

    print(str(x) + ": " + str(horizontal) + ", " + str(depth) + ", " + str(aim))

result = horizontal*depth

print(result)