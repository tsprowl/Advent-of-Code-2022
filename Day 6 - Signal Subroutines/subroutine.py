f = open("input.txt", "r")
input = []

for x in f:
    input = list(x)


def markerDetecter(signal, first, last):
    i = 0
    
    while i < len(signal):
        tester = signal[first:last]
        if len(tester) > len(set(tester)):
            first += 1
            last += 1
        else:
            return last
            break

def main():
    startOfPacket = markerDetecter(input, 0, 4)
    startOfMessage = markerDetecter(input, 0, 14)

    print("Start-of-packet marker detected after processing " + str(startOfPacket) + " characters.")
    print("Start-of-message marker detected after processing " + str(startOfMessage) + " characters.")

main()