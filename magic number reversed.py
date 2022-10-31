#124 ---> 1^1 + 2^2 + 4^3 = 69
#213 ---> 2^1 + 1^2 + 3^3 = 30


n = 213
l = 0
result = 0
c=n

while c>0:
    c = c//10
    l+=1



while n>0:
    result += (n%10)**l
    l -= 1
    n = n//10


print(result)
#magic number without in built functions
