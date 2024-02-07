list=[1,2,4,5,3]
n=len(list)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j] > list[j+1]:
             #   q=list[j]
              #  list[j] = list[j+1]
               # list[j+1] = q
            list[j] , list[j+1] = list[j+1] , list[j]
print ("sorted list",list)
a=sum(list)
print("SUM OF THE LIST IS:", a)

