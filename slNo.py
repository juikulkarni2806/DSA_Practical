n=int(input("Enter how many elements: "))
a=[]
for i in range(n):
    num=int(input("Enter Your Numbers: "))
    a.append(num)

min=a[0]
max=a[0]
smin=a[0]
smax=a[0]
for i in a:
    if i<min:
        smin=min
        min=i

    if i>max:
        smax=max
        max=i
print("smin= ",smin)
print("min= ",min)
print("smax= ",smax)
print("max= ",max)
