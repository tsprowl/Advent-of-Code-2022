valueDictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

f = open("input.txt", "r")
lines = []


def fileLines():
    for x in f:
        lineHolder = x.strip('\n')
        lines.append(lineHolder)


def commonFinder(string1, string2):
    commonList = []
    for x in string1:
        if x in string2:
            commonList.append(x)
    return commonList


def mixUpFinder():
    sumPriority = 0

    for x in lines:
        lineLength = len(x) // 2
        line1 = x[:lineLength]
        line2 = x[lineLength:]

        commonChar = commonFinder(line1, line2)[0]
        sumPriority += valueDictionary[commonChar]

    return sumPriority


def badgeFinder():
    sumPriority = 0
    lineList = []
    for x in lines:
        lineList.append(x)
    
    for z in range(0, len(lineList), 3):
        line1 = lineList[z]
        line2 = lineList[z+1]
        line3 = lineList[z+2]

        twoCommon = commonFinder(line1, line2)

        for x in twoCommon:
            if x in line3:
                sumPriority += valueDictionary[x]
                break

    return sumPriority


def main():
    fileLines()
    print("Part 1 Answer: ", mixUpFinder())
    print("Part 2 Answer: ", badgeFinder())

main()