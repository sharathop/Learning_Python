# def squres(nums):
#     result=[]
#     for i in nums:
#         result.append(i*i)
#     return result
    
# num= [1,2,3,4,5]
# print(squres(num))


# result =((x*x for x in range(6)))
# print(list(result))

# print(type(result))
# print(list(result))


# def process_numbers(nums):
#     for n in nums:
#         if n % 2 == 0:
#             yield n * 2
#         else:
#             yield n * 3
        
# gen=process_numbers(range(10))

# print (next(gen))
# print (next(gen))

import sys

# List comprehension
list_comp = [x*x for x in range(1000000)]

# Generator expression
gen_exp = (x*x for x in range(1000000))

print("List size:", sys.getsizeof(list_comp))
print("Generator size:", sys.getsizeof(gen_exp))