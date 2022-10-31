#29 --> 2+9=11 --> 1+1=2 #not equal to 1, not magic number
#19 --> 1+9=10 --> 1+0=1 #equal to 1, magic number
lst = []

for n in range(1, 3000):
    a = n
    sum_ = 0


    while True:
        while n>0:
            sum_ += n%10
            n=n//10

        if sum_ >= 10:
            n = sum_
            sum_ = 0
        else:
            break

    #print("Magic number:", sum_==1)
    if sum_ == 1:
        lst.append(a)


print(lst)
#print(sum_)
