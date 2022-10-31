n=1259060977
#n=125
c=1
sum_=0

while n>0:
    r=n%10
    sum_ += r*c
    n=n//10
    c+=1

if sum_%11 == 0: print("legal")
else: print("illegal")


#print(sum_)  
