A = int(input())
for i in range(A,1,-1):
    for j in range(i-1):
        print(" ", end = '')
    for k in range(0,A+1-i):
        print("*", end = '')
    print()
for b in range(0,A):
    print("*", end = '')