"""
Sort

Merge Sort

Split all values in the array into their own list
merge lists together
untill there is only a single list

"""

def Merge_Sort(array, show):

    def Show_Values():
        if show == True:
            print("Sorted || unsorted")
            print(finalArray, " || ", array)


    #Split all array values into their own list:
    layer0 = []
    for i in range(0,len(array)-1):




    print(array)

    

arrayInp = input("input an unordered list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
display = bool(input("Show process? (True/False): "))
Merge_Sort(arrayInp, display)



