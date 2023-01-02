instructions = []
screen = []
cycleCounter = 0
xRegister = 1
returnCount = 20
returnVal = 0

# Checks the state of the xRegister at certain values
def checkNums(value):
    global returnCount
    global returnVal
    if cycleCounter == returnCount:
        returnCount += 40
        temp = cycleCounter * value
        returnVal += temp

# Compares sprite and cycle info to determine the render
def crtRender(register, cycle):
    while (cycle >= 40):
        cycle -= 40
    if cycle == register:
        screen.append('#')
    elif cycle == register - 1:
        screen.append('#')
    elif cycle == register + 1:
        screen.append('#')
    else:
        screen.append('.')

# Modifies the render to appear in a visible manner
def printRender(renderList):
    counter = 0
    holder = ""
    for x in renderList:
        holder = holder + x
        counter += 1
        if counter >= 40:
            print(holder)
            holder = ""
            counter = 0



def main():
    global xRegister
    global cycleCounter

    f = open("input.txt", "r")
    for x in f:
        holder = x.strip('\n')
        instructions.append(holder)

    for v in instructions:
        if v == "noop":
            crtRender(xRegister, cycleCounter)
            cycleCounter += 1
            checkNums(xRegister)

        if v.__contains__("addx"):
            num = int(v.strip("addx "))

            crtRender(xRegister, cycleCounter)
            cycleCounter += 1
            checkNums(xRegister)

            crtRender(xRegister, cycleCounter)
            cycleCounter += 1
            checkNums(xRegister)

            xRegister += num

    printRender(screen)

main()