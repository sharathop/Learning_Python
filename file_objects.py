# # f=open('ai.txt')

# with open('ai.txt', 'r') as f:

#     # conent = f.readline(10)

#     # 

#     # conent = f.readline(10)

#     # print(conent)      
# # print(f.closed)
#     content = f.read(10)
#     print(content)
#     # print(len(content))
#     f.seek(0)

#     # content = f.read(10)
#     print(content)

#     # while len(content) > 0:
#     #     print(content,end='')
#     #     content = f.read(10)


# with open('test.txt', 'r') as f:
    
#     f.write('Sharath\n')
#     f.seek(3)
#     f.write('6')

    


with open('ai.txt','r') as fr:
    with open ('ai.txt_copy','w') as fw:
        for data in fr:
            fw.write(data)
