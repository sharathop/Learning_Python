# # # x = 6
# # # lr=0.1
# # # for i in range(20):
# # #     grad = 2*x

# # #     x = x-lr*grad
# # #     print(x)


# # def f(X):
# #     return X**2

# # X=3
# # h=0.00001

# # rsult=(f(X+h)-f(X))/h
# # print(rsult)

# W = 0
# x = 5
# y = 15
# b = 0 
# lr =0.01

# def predict(w,x,b):
#     return w*x +b

# def loss(w,b):
#     return (predict(w,x,b)-y)**2

# def derivative(w,b):
#     error = predict(w,x,b)-y
#     dl_dw = 2*error*x
#     dl_db =2*error
#     return dl_dw,dl_db

# for step in range(10):
#     print("*" * 50)

#     pred = predict(W,x,b)
#     ls=loss(W,b)
#     error = pred -y

#     dl_dw,dl_db=derivative(W,b)




#     print("prediction",pred)
#     print("loss",ls)
#     print("derivative",dl_dw,dl_db)

#     W = W -lr * dl_dw
#     b = b- lr * dl_db
# print("***********************************************************")
# print("new weight",W,'\n',"new_bias",b)
# print("prediction",pred,'\n',"loss",ls)


import numpy as np
x = np.array([1000,3,5,10],dtype=float)
x = x /x.max()
w=  np.zeros(4)
y =20000.0
b = 0
lr = 0.001

def predict(w,x,b):
    return x @ w +b

def loss(pred,y):
    return (pred - y )**2

def derivative(pred,y):
    error = pred-y
    dl_dw = 2 * error * x
    dl_db = 2 * error
    return dl_dw,dl_db

for i in range(100):

    
    

    
        print("*" * 30)

        pred = predict(w,x,b)
        ls = loss(pred,y)
        dl_dw,dl_db= derivative(pred,y)
        print(i)

        print(f"weight: {w}")
        print(f"b: {b}")
        print(f"prediction: {pred}")
        print(f"loss: {ls}")
        print(f"derivative:{dl_dw}")
        print(f"Bias: {dl_db}")
                                
        w = w -lr * dl_dw
        b = b - lr *dl_db

        if(ls<1):
             break

print("*"* 30)

print(f"actal :{y}")

print(f"weight: {w}")
print(f"b: {b}")
print(f"prediction: {pred}")
print(f"prediction: {predict(w,x,b)}")
print(f"loss: {ls}")
print(f"loss: {loss(pred,y)}")

print(f"derivative:{dl_dw,dl_db}")
print(f"derivative:{derivative(pred,y)}")