numbers = [273, 103, 5, 32, 65, 72, 800, 99]
sum1 = 0
sum2 = 0

for number in numbers:
    if number % 2 == 0:
        sum1 = sum1 + number
    elif number % 2 == 1:
        sum2 = sum2 + number
print("짝수의 합 : " ,sum1)
print("홀수의 합 : " ,sum2)