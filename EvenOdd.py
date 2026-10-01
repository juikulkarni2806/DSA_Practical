n=int(input("Enter How many numbers: "))
a=[]
for i in range(n):
    num=int(input("Enter Your Elements: "))
    a.append(num)
odd=[0]
even=[0]
ocount=0
ecount=0
for i in a:
    if(i%2==0):
        ecount+=1

    else:
        ocount+=1

print("Odd Numbers: ",ocount)
print("Even Numbers: ",ecount)
