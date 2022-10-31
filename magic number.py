#124 ---> 1^3 + 2^2 + 4^1 = 9
#213 ---> 2^3 + 1^2 + 3^1 = 12


n = 213
l = 0
result = 0

while n>0:
    #print(n)
    c = n%10
    n=n//10
    l+=1
    #print(c)

    result += c**l

print(result)


#magic number without in built functions
