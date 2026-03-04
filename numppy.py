# import numpy as np

# # a=np.array([5,8,9,4,6,2])
# # # print(a)

# b= np.array([[1,2,3,4],
#              [5,6,7,8,]])
# # # print(b)
# # # print(a[::3])
# # # print(a[::-1])

# # # print(b[:,::-1])
# # # print(b[:, ::-1])
# # # print(b[::-1,:])
# # # print(b[:,3])
# # # print(a.ndim)
# # # print(b.ndim)
# # # print(a.shape)
# # # print(b.shape)
# # # b[1,2]=71
# # # print(b)


# # #3d

# c=np.array([[[10,20],
#              [30,40],
#              [50,60],
#              [70,80]],

#              [[1,2],
#               [3,4],
#               [5,6],
#               [7,8]]])

# # # print(c.shape)
# # # print(c.ndim)

# # # print(c[:,::-1,::-1])


# # #intilizing arrays

# # zero=np.zeros((3,2))
# # print(zero)

# # ones=np.ones((3,4))
# # print(ones)

# # any=np.full(a.shape,66)
# # print(any)

# # any=np.full_like(a,6)

# # print(np.random.rand(2,2))

# # print(np.random.randint(2, size=(3,3)))
# # a=np.ones((5,5))
# # a[1:4,1:4] = 0
# # print(a)
# # a[2,2]=9
# # print(a)


# # n=np.array([1,2,3])
# # # print(n)
# # # n+=2
# # # print(n)


# # m=np.array([1,2,3])

# # print(n+m)
# z=np.sum(c,axis=0)
# print(z)
# z=np.sum(c,axis=1)
# print(z)
# z=np.sum(c,axis=2)
# print(z)
# #linear Algebra


import numpy as np

a =np.ones([2,3],dtype=int)
b=np.random.randint(0,10,size=(3,2))
print(b)

# print (a)
# print(b)

# multi =np.matmul(a,b)
# print(multi)

# nm=np.identity(3)

# print(nm)
mmm=np.dot(a,b)

print(mmm)