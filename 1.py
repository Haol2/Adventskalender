import copy

f = open("input1.txt", "r")

list = f.read().split()

cnt = 0
for i in range(1, len(list)):
    if (int(list[i]) > int(list[i-1])):
        cnt = cnt + 1

print("a1: " + str(cnt))

list2 = []
for i in range(0, len(list)-2):
    list2.append(int(list[i]) + int(list[i+1]) + int(list[i+2]))

cnt = 0
for i in range(1, len(list2)):
    if (int(list2[i]) > int(list2[i-1])):
        cnt = cnt + 1

print("a2: " + str(cnt))