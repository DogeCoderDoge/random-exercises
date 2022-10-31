#1
#12
#123
#1234
#12345

n = int(input("Number: "))
c=1 #c=2

for i in range(n):
    #print("test")
    for j in range(1,c+1):
        print(j, end="")

    c+=1
    print("")
