# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lissts are part of the collectiuons family
#in python
#creating a list
my_list = [1, 2, 3, 4,]
print(my_list) #1, 2, 3, 4, 5]
print(len(my_list)) #5
print(type(my_list))#<class 'list'>
print(my_list[0]) # 1
print(my_list [1:4]) #2, 3, 4, 
print(my_list[1:]) # everythinbg afdter 1
print(my_list[:-1]) #everything but the last one
#adds numbers to the end of your list
print(my_list[::-1]) #reverses my list
my_list.append(6) #adds 6 to the end of the list
print(my_list)
#add seven and eight to the end of the list
my_list.extend([7, 8])
print(my_list)
my_list.extend([9, 10, 11])
print(my_list)
#removes part of your list
my_list.pop(2) #removes a specified part of your list
print(my_list)
#reverse the list
my_list.reverse() #reverses the entire list
print(my_list)
#remove a specific number
my_list.reverse()
my_list.remove(4) #removes a specified number
my_list.remove(1)
print(my_list)
#add 50 more top the end of the string
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
my_list.extend(new_list)
#add more characters
new_list = list(range( 120-300))
print(new_list)
my_list.append(new_list)
print(my_list)
#print every 3rd number on your list
print(my_list[ : : 3])
print(my_list)
#print every 10 numbers
print(my_list[ : : 10])
#remove every 3rd element
del my_list[ : : 3]
print(len(my_list))
print(my_list)
#list functions
#.append() - adds and item to the end of the list
# .extend() - adds mulktiple items to the end of the list
# .pop() - removes and returns an item at a given index
#      (derfault is the last item)
# .remove() - removes the first occurence of a specific value
# .sort() -sorts the list in ascending order
# .reverse() - reverses the order of the list
#why is a list more important than a vbariable?
#a list can hold multiple values,
# while a variable can hold only one value at a time
cakes= [ 'chocolate' , 'vanilla', 'red velvet', 'carrot']
print(cakes)
#access the first item
print(cakes[0]) #chocolate
#access the last item
print(cakes[-1]) #carrot
#want two chocolate instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
cakes[1] = 'chocolate'
print(cakes)
#remove the last cake
cakes.pop()
print(cakes)
#insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fav_food = [ 'french fries', 'mac and cheese', 'cookie', 'chicken sandwich', 'pickles']
# Print the second and last item.
print(fav_food[0])
print(fav_food[4])
# Add a new item using .append().
fav_food.append('wings')
print(fav_food)
# Remove the first item using .pop(0).
fav_food.pop(0)
print(fav_food)
# Reverse your list using .reverse().
fav_food.reverse()
print(fav_food)

# sets = {1, 2, 3}
#setd are unordered collections of unique items
# sets do not support indexing or slicing
#sets do not support indexes or slices
# sets are mutable, meaning you can add or remove items
#sets are created using curly brackets {}
#do all sets allow duplicate items?
my_set= {1, 2, 4, 5, 6}
print(my_set)
print(type(my_set))
#add an item to the set
my_set.add(6)
print(my_set)
#remove an item from the set
my_set.remove(4)
print(my_set)

#check if an item is in the set
print(4 in my_set) #true
print(3 in my_set) #false

#tuples are ordered collkections of items
# tuples are immutable, meaning you cannot modigfy after creation
# tuples are created using ()
my_tuple = (1, 2, 3, 4, 5,)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
#try to modify the tuple (will raise an error)
