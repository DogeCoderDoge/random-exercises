'''
****1
***21
**321
*4321
54321
'''

n = int(input("Number: "))
stars = n-1

for i in range(n):
    for j in range(stars):
        print('*', end="")

    for k in range(n-stars,0,-1):
        print(k, end="")
    
    print("")
    stars-=1    
