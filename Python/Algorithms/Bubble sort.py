#Bubble sort
#create unordered list from input

valueList = []
valueString = ""
pointerPos = 0

valueString = input("enter list of numbers only, max 10: ")
if len(valueString) > 10:
    quit

i = 0
for i in range(0, len(valueString)):
    valueList.insert(i, valueString[i])
    
print(valueList)

#for each in list
#if the vlaue to the right is less that current value swap & set swap flag to true




def loopfunc(listvalue):
    swapMade = False
    for x in range(0, len(listvalue) - 1):
        if listvalue[x + 1] < listvalue[x]:
            swapMade = True
            tmp1 = listvalue[x]
            tmp2 = listvalue[x + 1]
            


            listvalue[x] = tmp2
            listvalue[x + 1] = tmp1
            
        print(listvalue)
    
        
    if swapMade == True:
        
        loopfunc(listvalue)

loopfunc(valueList)



        #'print("del value" + valueList[i + 2])
#del valueList[i + 2]






#pointer += 1
#if end then if flag = true set to false and repeat
#if flag = false at end then fin
