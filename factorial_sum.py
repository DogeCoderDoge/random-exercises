# 4! = 4*3*2*1

#5 --> 1! + 2! + 3! + 4! + 5!
#3 --> 1! + 2! + 3! = 9

num = int(input("Number: "))
answer = 0

def factorial(n):
    f = 1
    while n>0:
        f= f*n
        n-=1

    return f

while num>0:
    answer += factorial(num)
    #print(factorial(num))
    num-=1

print(answer)
