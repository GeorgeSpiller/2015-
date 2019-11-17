#get list of items
valueList = []
sortedList = []
unsortedList = []
i = 0
placeHolder = int(0)

valueString = input("enter list of numbers only, max 10: ")
if len(valueString) > 8:
    print("max 8 char")
    quit
#make the first item part of the sorted list
#and all others in the unsorted list


for i in range(1, len(valueString)):
    unsortedList.insert(i, valueString[i])

sortedList.append(valueString[0])
    
print(sortedList, unsortedList)

#whlie there are items in the unsorted list
#take first unsorted item
#while there is an item to the left of this item that is smaller
#swap with that item
#end
#end

while len(unsortedList) != 0:
    for pos in range(0, len(sortedList)):
        print("sorted pointer: ", pos)
        print("if ", sortedList[pos], " > ", unsortedList[0])
        
        if (sortedList[pos] > unsortedList[0]): # WHATS WRONG WITH THIS OMGGGGGGGG
            
            print("Within If")
            sortedList.insert(pos - 1, unsortedList[0])
            del unsortedList[0]               
    
    print(sortedList, unsortedList) 



















