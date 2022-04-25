print("보기(display)")
print("A - ADD")
print("S-Subtract")
print("M-Multiply")
print("D-Division")
num = input("A/S/M/D 중에서 연산 방법을 선택합니다.")
X,Y = map(int, input().split())
if num == 'A':
    print("Select: ",num)
    print('x,y input Data : ',X,Y)
    print(X+Y)
elif num == 'S':
    print("Select: ",num)
    print('x,y input Data : ',X,Y)
    print(X-Y)
elif num == 'M':
    print("Select: ",num)
    print('x,y input Data : ',X,Y)
    print(X*Y)
elif num == 'D':
    print("Select: ",num)
    print('x,y input Data : ',X,Y)
    print(X/Y)


