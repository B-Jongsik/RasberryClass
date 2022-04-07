A = int(input())
count = 0
num = A

while True :
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10)+c
    count = count +1
    if (num == A):
        break
print(count)