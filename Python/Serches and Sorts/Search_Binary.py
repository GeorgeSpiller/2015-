"""
Search

Binary Search:

Search through an ordered list by setting a start point(SP) at possition 0, an
end point (EP) at the end of the array, and a mid point (MP) in the middle.
Compare the value at the MP, and move the EP to the MP if the value is > MP, or
the SP to the MP if the value is < MP. Recalculate the MP and repeat the process
untill MP = value, or untill SP OR EP = MP.

"""

def Binary_Search(array, search, show):
    SP = 0
    EP = len(array)
    MP = int(EP / 2)
    found = False
    
    def Show_Values():
        if show == True:
            print(" SP = ", SP, " \n MP = ", MP, "\n EP = ", EP,)
            print("Found: ", found)
            print(array[SP:EP])
    Show_Values()
    
    for loop in range(0,len(array)):
        if array[MP] == search:
            found = True
            Show_Values()
            print(" Value found: ", search, " \n Possition: ", MP)
            break
        elif array[MP] < search:
            SP = MP
            MP = int( (SP + EP) / 2 )
            Show_Values()
        elif array[MP] > search:
            EP = MP
            MP = int( (SP + EP) / 2 )
            Show_Values()



arrayInp = input("input an ordered list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
search_value = input("Input a value to search for: ")
display = bool(input("Show process? (True/False): "))

Binary_Search(arrayInp, search_value, display)








