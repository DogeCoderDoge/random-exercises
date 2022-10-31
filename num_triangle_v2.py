#1
#23
#456
#78910

n = int(input("Number: "))
c=0

for i in range(n+1):
    for j in range(c,c+i):
        print(j, end="")

    c+=1
    print("")
