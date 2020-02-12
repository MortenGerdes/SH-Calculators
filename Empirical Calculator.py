import math
import time
import random

if __name__ == '__main__':
    print("==========================================================")
    print("Welcome to Morten's Secret Hitler probability calculator")
    print("==========================================================")
    print("")

    while(True):
        amountOfFasc = input("Enter amount of Fascist Cards: ")
        amountOfFasc = int(amountOfFasc)
        amountOfLib = input("Enter amount of Liberal Cards: ")
        amountOfLib = int(amountOfLib)
        drawToCount = input("Enter how many libs which should appear in a draw: ")
        drawToCount = int(drawToCount)
        drawSize = input("Enter draw size: ")
        drawSize = int(drawSize)
        specificDraw = input("What draw, 1 to " + str(math.floor((amountOfFasc+amountOfLib)/(drawSize))) + " should be counted? (0 for all): ")
        specificDraw = int(specificDraw)
        iterations = input("Enter how many games should be simulated: ")
        iterations = int(iterations)
        total = amountOfLib + amountOfFasc
        print("Amount of Fasc =", amountOfFasc, "and amount of Libs =", amountOfLib, "Total = " + str(total))
        print("Simulating", iterations, "games of Secret Hitler...")

        globalCounter = 0
        for epoc in range(0, iterations):
            drawPile = []
            for fasc in range(0, amountOfFasc):
                drawPile.append("F")

            for lib in range(0, amountOfLib):
                drawPile.append("L")
            random.shuffle(drawPile)
            drawPile = [drawPile[x:x+drawSize] for x in range(0, len(drawPile), drawSize)]

            for index, draws in enumerate(drawPile, start=1):
                libsFound = 0
                #print("draw = ", draws)
                if len(draws) != drawSize:
                    #print(len(draws))
                    #print("went here")
                    continue

                if specificDraw != 0:
                    if index != specificDraw:
                        continue

                for policy in draws:
                    if policy == "L":
                        libsFound += 1

                if libsFound == drawToCount:
                    #print("Found!")
                    #time.sleep(3)
                    #print("Counted:", draws , "len =" , len(draws))
                    globalCounter += 1
                    break
            #print(drawPile)
        print("Drawing " + str(drawToCount) + " libs in", iterations,  "draws happened " + str((globalCounter/iterations)*100) + "% of the times.")
        input("Done...")
    #print("")