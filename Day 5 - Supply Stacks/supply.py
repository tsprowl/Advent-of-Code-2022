f = open("input.txt", "r")
list1 = list()
list2 = list()
list3 = list()
list4 = list()
list5 = list()
list6 = list()
list7 = list()
list8 = list()
list9 = list()
listHolder = [list1, list2, list3, list4, list5, list6, list7, list8, list9]
moveHolder = []

# Clears out the whitespace and lingering data from columnGenerator()
def columnCleanup(list):
    list.pop(-1)
    list.reverse()
    spaceCount = 0
    for x in list:
        if x.isspace():
            spaceCount += 1
    while spaceCount > 0:
        for z in list:
            if z.isspace():
                list.pop()
                spaceCount -=1


# Scans the file line by line, separating the crate structure and move list            
def columnGenerator():
    for x in f:
        temp = x

        # Crates
        if len(temp) == 36:
            list1.append(temp[0:3])
            list2.append(temp[4:7])
            list3.append(temp[8:11])
            list4.append(temp[12:15])
            list5.append(temp[16:19])
            list6.append(temp[20:23])
            list7.append(temp[24:27])
            list8.append(temp[28:31])
            list9.append(temp[32:35])    
        elif len(temp) != 1:

            # Moves
            if len(temp) == 19:
                moveNum = int(temp[5])
                start = int(temp[12]) - 1
                end = int(temp[17]) - 1
                moveList = [start, end, moveNum]
                moveHolder.append(moveList)
            elif len(temp) == 20:
                moveNum = int(temp[5:7])
                start = int(temp[13]) - 1
                end = int(temp[18]) - 1
                moveList = [start, end, moveNum]
                moveHolder.append(moveList)
    for z in listHolder:
        columnCleanup(z)


# Makes moves when you can only move one crate at a time
def moveMaker1(start, end, crateNum):
    startCol = listHolder[start]
    endCol = listHolder[end]
    i = 0

    while i < crateNum:
        holder = startCol.pop()
        endCol.append(holder)
        i += 1


# Makes moves when you can move multiple crates at once
def moveMaker2(start, end, crateNum):
    startCol = listHolder[start]
    endCol = listHolder[end]
    stackHolder = []
    i = 0

    while i < crateNum:
        temp = startCol.pop()
        stackHolder.append(temp)
        i += 1
    
    while len(stackHolder) != 0:
        holder = stackHolder.pop()
        endCol.append(holder)
    

# Returns the final formatted answer
def finalCrates():
    answer = ""
    for q in listHolder:
        temp = q.pop()
        temp = temp.strip("[]")
        answer = answer + temp
    return answer

def main():
    probPart = int(input("Enter the corresponding Part Number to solve that part of the problem: "))
    columnGenerator()
    if (probPart == 1):
        for l in moveHolder:
          moveMaker1(l[0], l[1], l[2])
    elif (probPart == 2 ):
        for l in moveHolder:
            moveMaker2(l[0], l[1], l[2])
    print("The answer for Part " + str(probPart) + " is: " + finalCrates())
            
main()