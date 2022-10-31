#123 ---> 321 ---> not palendrome
#121 ---> 121 ---> palendrome
#637 ---> 736 ---> not palendrome

n = 123
c = n
rev = 0

while n > 0:
    r=n%10 #1
    rev = rev*10 + r #321
    n = n//10 #0
    
print(rev==n)
if rev == c: print("palendrome")
else: print("no palendrome")

