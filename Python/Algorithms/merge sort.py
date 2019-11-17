#merge sort

valueList = []
finalList = []

valueString = input("enter list of numbers only, max 8: ")
if len(valueString) > 8:
    print("max 8 char")
    quit

i = 0
for i in range(0, len(valueString)):
    valueList.insert(i, valueString[i])

print(valueList)

def mergeList(list1, list2):
    finalList = []
    i = 0
    while (len(list1) != 0) and (len(list2) != 0):
        
        if list1[i] < list2[i]:
            finalList.append(list1[i])
            del list1[i]
        else:
            finalList.append(list2[i])
            del list2[i]
    i = 0

    if len(list1) == 0:
        for a in range(0, len(list2)):
            finalList.append(list2[a])
    else:
        for b in range(0, len(list1)):
            finalList.append(list1[b])

    return finalList


#split n items into  n lists of 1 item


lvl1 = []
lvl2 = []
lvl3 = []
lvl4 = []
lvl5 = []
lvl6 = []
lvl7 = []


la=[]
lb=[]
lc=[]
ld=[]
le=[]
lf=[]
lg=[]
lh=[]
li=[]
lj=[]
lk=[]


#Max 10
if len(valueList) == 1:
    print("invalid list")
elif len(valueList) == 2:
    la.append(valueList[0])
    lb.append(valueList[1])
    print("single lists: ", la, lb)
    finalList = mergeList(la, lb)
elif len(valueList) == 3:    
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    print("single lists: ", la, lb, lc)
    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc)
    finalList = mergeList(lvl1,lc)
elif len(valueList) == 4:
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    ld.append(valueList[3])
    print("single lists: ", la, lb, lc, ld)
    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc, ld)
    lvl2 = mergeList(lc, ld)
    print("merge lists: ", lvl1, lvl2)
    finalList = mergeList(lvl1, lvl2)

elif len(valueList) == 5:
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    ld.append(valueList[3])
    le.append(valueList[4])
    print("single lists: ", la, lb, lc, ld, le)

    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc, ld, le)
    lvl2 = mergeList(lc, ld)
    print("merge lists: ", lvl1, lvl2, "#", le)
    lvl3 = mergeList(lvl2, le)
    print("merge lists: ", lvl1, lvl3, "#")
    finalList = mergeList(lvl1, lvl3)
    
elif len(valueList) == 6:
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    ld.append(valueList[3])
    le.append(valueList[4])
    lf.append(valueList[5])
    print("single lists: ", la, lb, lc, ld, le, lf)

    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc, ld, le)
    lvl2 = mergeList(lc, ld)
    print("merge lists: ", lvl1, lvl2, "#", le, lf)
    lvl3 = mergeList(le, lf)
    print("merge lists: ", lvl1, lvl2, lvl3, "#")
    lvl4 = mergeList(lvl1, lvl2)
    print("merge lists: ", lvl4, lvl3, "#")
    finalList = mergeList(lvl3, lvl4)

elif len(valueList) == 7:
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    ld.append(valueList[3])
    le.append(valueList[4])
    lf.append(valueList[5])
    lg.append(valueList[6])
    print("single lists: ", la, lb, lc, ld, le, lf, lg)

    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc, ld, le, lg)
    lvl2 = mergeList(lc, ld)
    print("merge lists: ", lvl1, lvl2, "#", le, lf, lg)
    lvl3 = mergeList(le, lf)
    print("merge lists: ", lvl1, lvl2, lvl3, "#", lg)
    lvl4 = mergeList(lvl3, lg)
    print("merge lists: ", lvl1, lvl2, lvl4, "#")
    lvl5 = mergeList(lvl1, lvl2)
    print("merge lists: ", lvl5, lvl4, "#")
    finalList = mergeList(lvl4, lvl5)
        
elif len(valueList) == 8:
    la.append(valueList[0])
    lb.append(valueList[1])
    lc.append(valueList[2])
    ld.append(valueList[3])
    le.append(valueList[4])
    lf.append(valueList[5])
    lg.append(valueList[6])
    lh.append(valueList[7])
    print("single lists: ", la, lb, lc, ld, le, lf, lg, lh)

    lvl1 = mergeList(la, lb)
    print("merge lists: ", lvl1, "#", lc, ld, le, lg)
    lvl2 = mergeList(lc, ld)
    print("merge lists: ", lvl1, lvl2, "#", le, lf, lg)
    lvl3 = mergeList(le, lf)
    print("merge lists: ", lvl1, lvl2, lvl3, "#", lg, lh)
    lvl4 = mergeList(lg, lh)
    print("merge lists: ", lvl1, lvl2, lvl3, lvl4, "#")
    lvl5 = mergeList(lvl1, lvl2)
    print("merge lists: ", lvl5, lvl3, lvl4, "#")
    lvl6 = mergeList(lvl3, lvl4)
    print("merge lists: ", lvl5, lvl6, "#")
    finalList = mergeList(lvl5, lvl6)
else:
    print("invalid list length")


print(finalList)










#while there is more than 1 list
#pair up a list with eachother













    

