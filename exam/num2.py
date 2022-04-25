A = input()

A_list = list(map(int, str(A)))
B = len(A_list)

for i in A_list:
    print(B,":", i,end=", ")
    B = B - 1
