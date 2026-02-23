# List Documentation:
# Key Characteristics of Python Lists
# Ordered: The items in a list maintain a specific order, which does not change unless explicitly modified.
#  The first element has an index of 0.
# Mutable (Changeable): You can add, remove, or modify elements in a list after it has been created using various methods like append(), remove(), or index assignment.
# Heterogeneous: Lists can contain items of different data types within the same collection, including integers, strings, booleans, and even other lists or dictionaries.
# Allows Duplicates: Since elements are accessed by their index, a list can contain multiple items with the same value.
# Dynamic Size: Lists can grow or shrink in size as elements are added or removed during the program's execution.

List=['Sharath' , 23 , 600000, 'TVSRTX300', 'HOUSE', 'VIRTUS' ]

nums=[45,4523,40,401,105,]

list1=['Humble', 'good']
print(List[2])

print(List[0:4])

print(len(List))

print(List.insert(2,'Engineer'))
print(List.append('Gold'))
print(List)

# print(dir(list))
List.insert(-1,list1)

print(List)

List.extend(list1)
print(List)

List.remove(600000)
print(List)
popped=List.pop()
print(popped)

List.reverse()
print(List)
List.sort(key=str)
print(List)
nums.sort()

print(nums)
nums.sort(reverse=True)
print(nums)



sorted_nums=sorted(nums)

print(sorted_nums)

print(min(nums),max(nums))

for index, items in enumerate(List):
    print(index, items)
sep='* '.join(list1)
print(sep)

new_split=sep.split('*')
print(new_split)



#Tuples


# Creation
my_tuple = ('Sharath', 23, 'VIRTUS')
single_tuple = ('Gold',) # Note the comma! Without it, it's just a string.

# Accessing (Same as lists)
print(my_tuple[0])    # Output: Sharath
print(my_tuple[-1])   # Output: VIRTUS

# The "Locked" Nature
# my_tuple[1] = 24    # This would throw a TypeError!
# my_tuple.append(5)  # This doesn't exist!

#unpacking
name, age, car = my_tuple
print(name) # Sharath


# Methods
# Tuples only have two built-in methods because they can't be modified:
# count(): Returns the number of times a value occurs.
# index(): Searches for a value and returns its position.



for index, items in enumerate(my_tuple):
    print(index, items)

print(my_tuple.count('Sharath'))
print(my_tuple.index('VIRTUS'))


#Sets

# Creation
my_set = {'Sharath', 23, 'VIRTUS', 'Sharath'} 
print(my_set) # Output: {'VIRTUS', 'Sharath', 23} (Note: duplicate 'Sharath' is gone)

# Adding/Removing
my_set.add('Gold')         # Adds one item
my_set.update([10, 20])    # Adds multiple items from a list
my_set.remove(23)          # Removes '23' (throws error if not found)
my_set.discard('HOUSE')    # Removes 'HOUSE' (no error if not found)
print(my_set)


# Union and Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) # Output: {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set) # Output: {3}

# Difference    
difference_set = set1.difference(set2)
print(difference_set) # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) # Output: {1, 2, 4, 5}

# Subset and Superset
subset_set = {1, 2}
superset_set = {1, 2, 3, 4, 5}
print(subset_set.issubset(superset_set)) # Output: True
print(superset_set.issuperset(subset_set)) # Output: True


