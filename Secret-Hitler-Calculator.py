import math

def binomial(n, x):
    if n < x:
        return 0
    return (math.factorial(n))/(math.factorial(x) * math.factorial(n-x))

if __name__ == '__main__':
    print("==========================================================")
    print("Welcome to Morten's Secret Hitler probability calculator")
    print("==========================================================")
    print("")

    while True:

        amountOfFasc = input("Enter amount of Fascist Cards: ")
        amountOfFasc = int(amountOfFasc)
        amountOfLib = input("Enter amount of Liberal Cards: ")
        amountOfLib = int(amountOfLib)
        amountToDraw = input("Enter amount of cards to draw: ")
        amountToDraw = int(amountToDraw)
        total = amountOfLib + amountOfFasc

        print("Amount of Fasc =", amountOfFasc, "and amount of Libs =", amountOfLib, "Total = " + str(total))
        print("")

        for draw in range(amountToDraw+1):
            localAOL = (amountToDraw-draw) % (amountToDraw+1)
            localAOF = draw % (amountToDraw+1)
            if(localAOF > amountOfFasc or localAOL > amountOfLib):
                continue
            chance = (binomial(amountOfFasc, localAOF) * binomial(total - amountOfFasc, amountToDraw - localAOF))/binomial(total, amountToDraw)
            print("Chance to draw {}F and {}L. Chance = {}%".format(localAOF, localAOL, chance*100))
        print("Chance of drawing atleast 1 lib: {}%".format((1-(binomial(amountOfFasc, amountToDraw) * binomial(total - amountOfFasc, amountToDraw - amountToDraw)) / binomial(total, amountToDraw))*100))
        input("Done...")
        print("")
        print("")