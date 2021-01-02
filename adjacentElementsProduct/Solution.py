def adjacentElementsProduct(inputArray):
    total=-10000000
    for i in range(len(inputArray)-1):
        if inputArray[i]*inputArray[1+i]>=total:
            total=inputArray[i]*inputArray[1+i]
    return total        
