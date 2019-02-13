numFN = 0
fns = []
upper = 0

def getNumFn():
    global numFN
    numFN = input("How many functions would you like to check?")

def getFn():
    for i in range(int(numFN)):
        fns.append((input("Enter a function:")))

def getUpper():
    global upper
    upper =  input("How much input would you like to test this on?")




