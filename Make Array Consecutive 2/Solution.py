def makeArrayConsecutive2(statues):
    arr=sorted(statues)
    addition=0
    for i in range(len(arr)-1):
        if arr[i]+1 in arr:
            pass
        else:
            addition+=arr[i+1]-arr[i]-1
    return addition