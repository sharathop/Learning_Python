List=['Sharath' , 23 , 600000, 'TVSRTX300', 'HOUSE', 'VIRTUS' ]

nums=[45,4523,40,401,105,]

list1=['Humble', 'good']
print(List[2])

print(List[0:4])

print(len(List))

# print(List.insert(2,'Engineer'))
# print(List.append('Gold'))
print(List)

#print(dir(list))
# List.insert(-1,list1)

# print(List)

List.extend(list1)

List.remove(600000)
popped=List.pop()
print(popped)

List.reverse()

List.sort(key=str)
nums.sort()

# print(nums)
# nums.sort(reverse=True)
# print(nums)

print(List)

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


