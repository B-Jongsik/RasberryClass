a = input()
b = input()
c = int(b)%10
d = (int(b)-int(c))%100
f = int(d)/10
e = (int(b)-int(c)-int(d))/100
print(int(a)*int(c))
print(int(a)*int(f))
print(int(a)*int(e))
print(int(a)*int(b))