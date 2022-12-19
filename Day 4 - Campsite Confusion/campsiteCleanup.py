f = open("input.txt", "r")

completeOverlapCount = 0
partialOverlapCount = 0

def isTotalOverlap(range1, range2):
    range1Start = int(range1[0])
    range1End = int(range1[1])

    range2Start = int(range2[0])
    range2End = int(range2[1])

    if (range1Start > range2Start):
        if (range1End <= range2End):
            return True
    elif (range2Start > range1Start):
        if (range2End <= range1End):
            return True
    elif (range1Start == range2Start):
        if (range1End >= range2End) or (range1End <= range2End):
            return True


def isPartialOverlap(range1, range2):
    range1Start = int(range1[0])
    range1End = int(range1[1])

    range2Start = int(range2[0])
    range2End = int(range2[1])

    if (isTotalOverlap(range1, range2) == True):
        return True
    elif (range1Start == range2Start) or (range1Start == range2End) or (range1End == range2Start) or (range1End == range2End):
        return True
    elif (range1Start > range2Start) and (range1Start < range2End):
        return True
    elif (range2Start > range1Start) and (range2Start < range1End):
        return True


for x in f:
    temp = x.strip('\n')
    sites = temp.split(",")

    siteA = sites[0].split("-")
    siteB = sites[1].split("-")

    if(isTotalOverlap(siteA, siteB)):
        completeOverlapCount += 1

    if(isPartialOverlap(siteA, siteB)):
        partialOverlapCount += 1

print("Part 1 Answer: ", completeOverlapCount)
print("Part 2 Answer: ", partialOverlapCount)

a1 = 7
b1 = 11

a1 -= b1

print(a1)