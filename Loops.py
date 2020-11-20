def addup(numList):
    total = 0
    for num in numList:
        total = total + num
        
    return total

def multiplyup(numList):
    total = 1
    for num in numList:
        total = total * num

    #for i in range(len(numList)):
    #    total = total * numList[i]
        
    return total

def ratWeight(weigthList1, weightList2):
    if len(weightList2) != len(weigthList1):
        print("Weigh lists are not the same size!")
        return
    for i in range(len(weightList2)):
        if weigthList1[i] > weightList2[i]:
            print("rat1 weighted more than rat2 on day {}".format(i+1))
        if weigthList1[i] < weightList2[i]:
            print("rat1 weighted less than rat2 on day {}".format(i+1))
        
    if weigthList1[0] > weightList2[0] and weigthList1[-1] > weightList2[-1]:
        print("Rat 1 remained heavier than Rat 2")
        return
    if weigthList1[0]> weightList2[0] and weigthList1[-1]< weightList2[-1]:
        print("Rat 2 became heavier than Rat 1")
        return
    else:
        print("Unknown weight gain or loss")
        
    return

def printRange(x ,y):
    for i in range(x, y+1):
        print(i)

def printDes(x,y):
    for i in range(y, x-1, -1):
        print(i, end=' ')

    print()

def addRange(x,y):
    total = 0
    for i in range(x,y+1):
        total = total + i
    print(total)


def removeNeg(numList):
    negList = []
    for item in numList:
        if item < 0:
            negList.append(item)

    for elem in negList:
        if elem in numList:
            numList.remove(elem)


def remNeg(numList):
    posList = []
    for item in numList:
        if item > 0:
            posList.append(item)

    return posList
        
            

            

 
if __name__ == "__main__":
    country_population = [1295, 345, 202, 8, 756, 1234]
    mySum = addup(country_population)
    print("total population: {}".format(mySum))
    myProduct = multiplyup(country_population)
    print("multiplied: {}".format(myProduct))
    
    weightL1 = [10, 14, 15]
    weightL2 = [23,25,7]
    ratWeight(weightL1, weightL2)

    printRange(33, 49)
    printDes(1,10)

    myList = [1,2,3,-3,6,-1,-3,1]
    #removeNeg(myList)
    print(remNeg(myList))


