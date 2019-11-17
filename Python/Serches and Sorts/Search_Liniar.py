"""
Search

Liniar Search:

Search through an ordered/unordered array sequentially for the desired value.
"""

def Liniar_Search(array, search):
    for i in range(0, len(array)):
        if array[i] == search:
            print(" Value found: ", search," \n Possition: ", i)
            found = True
        
    if found = False:
        print("Value ", search, " not found.")



found = False
arrayInp = input("input a list to search, separated by commas: ")
arrayInp = arrayInp.split(",")
print("Array: \n ", arrayInp)
search_value = input("input a value to search for: ")

Liniar_Search(arrayInp, search_value)
