#n = int(input("Bana piramit yuksekligini soyle"))
n = 5
for i in range(1, n+1):
    for j in range(0,i):
        print(i,end="")
    print("\r")

for i in range(1,n+1)[::-1]:
    for j in range(0,i):
        print(i,end="")
    print("\r")

for i in range(0,n)[::-1]:
    for j in range(0,i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print("\r")

for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print("\r")








