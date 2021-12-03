import copy

f = open("input3.txt", "r")

list = f.read().split()

gamma = ""
epsilon = ""

nulls = [0]*len(list[0])
ones = [0]*len(list[0])

for number in list:
    for i in range(len(number)):
        if (number[i] == "0"):
            nulls[i] += 1
        else:
            ones[i] += 1

print("number of 0's: " + str(nulls))
print("number of 1's: " + str(ones))

for i in range(len(nulls)):
    if (nulls[i] > ones[i]):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gammadec = int(gamma, 2)
epsilondec = int(epsilon, 2)
print("gamma rate: " + gamma + " = " + str(gammadec))
print("epsilon rate: " + epsilon + " = " + str(epsilondec))
print("power consumption: " + str(gammadec*epsilondec))

list2 = copy.deepcopy(list)

for i in range(len(list2[0])):
    #print("---------------------------------------------------------------------")
    #print("length = " + str(len(list2)))
    #print("i = " + str(i))
    #for number in list2:
     #   print(number)

    if (len(list2) == 1):
        break
    else:
        nulls = 0
        ones = 0
        for number in list2:
            if (number[i] == "0"):
                nulls += 1
            else:
                ones += 1

        if (ones >= nulls):
            max = "1"
        else:
            max = "0"

        list3 = []
        for number in list2:
            if (number[i] == max):
                list3.append(number)
        list2 = copy.deepcopy(list3)

oxval = list2[0]
oxvaldec = int(list2[0], 2)

list2 = copy.deepcopy(list)

for i in range(len(list2[0])):
    #print("---------------------------------------------------------------------")
    #print("length = " + str(len(list2)))
    #print("i = " + str(i))
    #for number in list2:
       #print(number)

    if (len(list2) == 1):
        break
    else:
        nulls = 0
        ones = 0
        for number in list2:
            if (number[i] == "0"):
                nulls += 1
            else:
                ones += 1

        if (ones >= nulls):
            min = "0"
        else:
            min = "1"

        list3 = []
        for number in list2:
            if (number[i] == min):
                list3.append(number)
        list2 = copy.deepcopy(list3)

co2val = list2[0]
co2valdec = int(list2[0], 2)

print("oxygen generator rating: " + oxval + " = " + str(oxvaldec))
print("CO2 scrubber rating: " + co2val + " = " + str(co2valdec))
print("life support rating: " + str(oxvaldec*co2valdec))