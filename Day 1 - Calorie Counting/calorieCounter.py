f = open("input.txt", "r")
holder = 0
calorieList = list(())
for x in f:
    temp = x.strip('\n')
    if temp != "":
        holder += int(temp)
    else:
        calorieList.append(holder)
        holder = 0
f.close()

calorieList.sort(reverse = True)
top3 = list((calorieList[0:3]))
print("Part 1 Answer: ", top3[0])

totalCal = 0
for i in top3:
    totalCal += i
print("Part 2 Answer: ", totalCal)

