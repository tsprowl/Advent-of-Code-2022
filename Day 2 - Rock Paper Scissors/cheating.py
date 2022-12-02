f = open("input.txt", "r")
first = ""
second = ""
points1 = 0
points2 = 0

# Converts a letter to a move type
def moveConverter(move):
    if move == "X" or move == "A":
        return "rock"
    elif move == "Y" or move == "B":
        return "paper"
    elif move == "Z" or move == "C":
        return "scissors"

# Converts a letter to a win condition
def conConverter(winCondition):
    if winCondition == "X":
        return "lose"
    elif winCondition == "Y":
        return "draw"
    elif winCondition == "Z":
        return "win"

# Returns the resulting win condition, given the opponent's move and your own
def matchupMoves(oppMove, yourMove):
    if oppMove == "rock":
        if yourMove == "rock":
            return "draw"
        elif yourMove == "paper":
            return "win"
        elif yourMove == "scissors":
            return "lose"
    elif oppMove == "paper":
        if yourMove == "rock":
            return "lose"
        elif yourMove == "paper":
            return "draw"
        elif yourMove == "scissors":
            return "win"
    if oppMove == "scissors":
        if yourMove == "rock":
            return "win"
        elif yourMove == "paper":
            return "lose"
        elif yourMove == "scissors":
            return "draw"

# Returns the move to make, given the opponent's move and the desired win condition
def matchupCon(oppMove, winCon):
    if oppMove == "rock":
        if winCon == "win":
            return "paper"
        elif winCon == "draw":
            return "rock"
        elif winCon == "lose":
            return "scissors"
    if oppMove == "paper":
        if winCon == "win":
            return "scissors"
        elif winCon == "draw":
            return "paper"
        elif winCon == "lose":
            return "rock"
    if oppMove == "scissors":
        if winCon == "win":
            return "rock"
        elif winCon == "draw":
            return "scissors"
        elif winCon == "lose":
            return "paper"

# Returns the point value of each win condition
def winCon (endGoal):
    if endGoal == "win":
        return 6
    elif endGoal == "draw":
        return 3
    else:
         return 0

# Returns the point value of each move
def makeMove (move):
    if move == "rock":
        return 1
    elif move == "paper":
        return 2
    elif move == "scissors":
        return 3


# in this case, version is which part of the problem you're trying to solve
def scoreCalc(first, second, version):
    roundPoints = 0
    if version == 1:
        oppMove = moveConverter(first)
        yourMove = moveConverter(second)

        roundPoints += makeMove(yourMove)
        roundPoints += winCon(matchupMoves(oppMove, yourMove))

    if version == 2:
        oppMove = moveConverter(first)
        winCondition = conConverter(second)

        roundPoints += winCon(winCondition)
        roundPoints += makeMove(matchupCon(oppMove, winCondition))

    return roundPoints


for x in f:
    first = x[0]
    second = x[2]
    points1 += scoreCalc(first, second, 1)
    points2 += scoreCalc(first, second, 2)

f.close()

print("Part 1 Answer: ", points1)
print("Part 2 Answer: ", points2)




