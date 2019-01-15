
list_1=[]
n=int(input('enter number of numbers  : '))
for i in range(n):
    list_1.append(int(input('enter number  : ')))



sum=0

y=lambda x:x+sum

for i in range(n):
   sum= y(list_1[i])

print(sum)

