nums =[1,2,3,4,5,6]

result=([n*n for n in nums])
print(result)

even =([n  for n in nums if n % 2 ==0])
print(even)

odd =([n*10 if n %2==0 else n for n in nums  ])
print(odd)


nors= [1,2,3,4,5]

ans = [{n:n*n} for n in nors ]

print(ans)

word ="python"

upper = ([n for n in word.upper()])
print(upper)

cube =[{n:n*n*n} for n in nors if  n %2  !=0]
print (cube)