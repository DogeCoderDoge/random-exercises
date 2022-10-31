#123 ---> 321

n = int(input("Number: "))
n1 = n
n2=n
result = 0
c=0

while n>0:
    n=n//10
    c+=1

while n1>0:
    c-=1
    r=n1%10
    result += r*(10**c)
    n1=n1//10
    print(r, c)

print(result, "is the reversed number")
#print(result==n2)

   
