# A program to print the list and totals for a Shopping List.
Shopping_List = {"Tissuse":10, "Toothpaste":50, "Apple":100}

# A for loop to print the list.
for value in Shopping_List:
    print(value,":", Shopping_List[value])

# To print the Totals of the Shopping List.
total = sum(Shopping_List.values())
print("------------------------------------------------")
print("The Total is:",total)
print("------------------------------------------------")