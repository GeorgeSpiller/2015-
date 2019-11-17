"""
Sort

Bubble Sort

Loop throught the unordered list and swap any values that are sequentially out
of order. If a swap has been made during the itteration, repeat the process.
"""

def Bubble_Sort(array, show):
    SwapMade = True
    
    def Show_Values():
        print("Swap Made: ", SwapMade)
        print(array)
    Show_Values()
    
    while SwapMade == True:
        SwapMade = False
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                SwapMade = True
        Show_Values()



arrayInp = input("input an unordered list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
display = bool(input("Show process? (True/False): "))
Bubble_Sort(arrayInp, display)








