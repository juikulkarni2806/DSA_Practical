n=int(input("How Many Numbers: "))
a=[]
for i in range(n):
    num=int(input("enter Your Numbers: "))
    a.append(num)

sum=0
for i in a:
    sum+=i
print(sum)
