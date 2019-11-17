"""
Sort

Insersion Sort


"""

def Insersion_Sort(array, show):
    finalArray = []
    def Show_Values():
        if show == True:
            print("Sorted || unsorted")
            print(finalArray, " || ", array)

    def Swap(val1, val2):
        tmp = finalArray[val1]
        finalArray[val1] = finalArray[val2]
        finalArray[val2] = tmp

    def sort():
        value_poss = len(finalArray) - 1
        for i in range(len(finalArray)-1, -1, -1):
            #print(finalArray[value_poss])
            #print(finalArray[value_poss]-1)
            if finalArray[value_poss] < finalArray[i]:
                Swap(value_poss, value_poss-1)
                value_poss -= 1
            else:
                continue


    finalArray.append(array[0])
    del array[0]
    Show_Values()
    while len(array) != 0:
        finalArray.append(array[0])
        del array[0]
        sort()
        Show_Values()

arrayInp = input("input an unordered list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
display = bool(input("Show process? (True/False): "))
Insersion_Sort(arrayInp, display)



