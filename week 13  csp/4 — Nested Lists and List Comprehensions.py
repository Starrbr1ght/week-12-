# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.
fruit =    ['apple', 'orange', 'banana', 'coconut']
vegetables=['celery', 'carrots', 'potatos']
meats=     ['chicken', 'fish', 'turkey']
groceries= [fruit, vegetables, meats]
# print(groceries[0][0]) #The first [] is either fruit, vege, or meats. (0,1,2)
# #second [] is which item from the list you want printed out
# print(groceries[2][2])
# print(groceries[1][2])

for collection in groceries
    for food in collection:
         print(food, end=' ')
         print()




# Key Notes:
num_pad = ((1, 2, 3,),
           (4, 5, 6,)
           (7, 8, 9,),
           ('*', 0, '#'))
# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
