"""
Sort

Quck Sort - Pivots

Get the first value (current value), itterate through the unsorted list and
place anything that is smaller than the current value to the left of it. Set
this value as a pivot, and then repeat for the next value.

"""

def Quick_Sort_Pivots(array, show):
    
    def Show_Values():
        if show == True:
            print(array)

    continueLoop = True
        
    while continueLoop == True:
        Show_Values()
        continueLoop = False
        for i in range(0, len(array)):
            if "P" in array[i]:
                continue
            elif "P" not in array[i]:
                current_value = array[i]
                current_value_poss = i
                array[current_value_poss] = array[current_value_poss] + "P"
                print("Current Value is ", current_value, " at poss: ", current_value_poss)
                Show_Values()
                break

        for x in range(0, len(array)-1):#
            if x == current_value_poss:
                for y in range(0, len(array)-1):#
                    if "P" in array[y]:
                        if array[x][0] > array[y][1]:
                            print(array[x], " > ", array[y])
                            continue
                        elif array[x][0] < array[y][1]:
                            print(array[x], " insert to poss ", y)
                            tmp = array[x]
                            del array[x]
                            array.insert(y, tmp)
                        else:
                            continue
                Show_Values()
            elif "P" in array[x]:
                continue
            else:
                print("the current value to be sorted amungst pivots is: ", array[x])
                for y in range(0, len(array)-1):#
                    if "P" in array[y]:
                        if array[x] > array[y][1]:
                            print(array[x], " > ", array[y])
                            continue
                        elif array[x] < array[y][1]:
                            print(array[x], " insert to poss ", y)
                            tmp = array[x]
                            del array[x]
                            array.insert(y, tmp)
                        else:
                            continue
                Show_Values()

        for i in range(0, len(array)):
            if "P" in array[i]:
                continue
            else:
                continueLoop = True

     
    """
    Get the first value (current value)
    itterate through the unsorted list
    place anything that is smaller than the current to left
    Set this value as a pivot
    repeat for the next value
    """

arrayInp = input("input an unordered list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
display = bool(input("Show process? (True/False): "))
print(len(arrayInp))
Quick_Sort_Pivots(arrayInp, display)




"""
            elif "P" not in array[i] and array[i] > current_value:
                print(array[i], " is bigger than ", current_value)
                print("Swap being made at pos ", i, " and poss ", current_value_poss)
                tmp = array[i]
                del array[i]
                array.insert(current_value_poss + 1, tmp)
                
                current_value_poss -= 1
                print("current value possition: ", current_value_poss)
                Show_Values()
            else:                
                continue
            
            elif "P" not in array[i] and array[i] < current_value:
                print(array[i], " is smaller than ", current_value)
                print("Swap being made at pos ", i, " and poss ", current_value_poss)
                tmp = array[i]
                del array[i]
                array.insert(current_value_poss, tmp)
                
                current_value_poss += 1
                print("current value possition: ", current_value_poss)
                Show_Values()
                """
