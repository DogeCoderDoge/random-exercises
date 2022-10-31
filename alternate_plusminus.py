#3 --> 1-2+3 = 2
#4 --> 1-2+3-4 = -2
#5 --> 1-2+3-4+5 = 3

n=5
c=0
sum_=0

while c < n:
    c+=1
    print(c)
    if c%2 == 0:
        sum_ -= c
    else: sum_ += c
    
print(sum_, "is the answer")


