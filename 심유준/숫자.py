num1 = int(input('첫 번째 숫자'))
num2 = int(input('두 번째 숫자'))
num3 = int(input('세 번째 숫자'))

if num1 >= num2:
    t = num1
elif num1 >= num3:
    t = num1
elif num2 >= num1:
    t = num2
elif num2 >= num3:
    t= num2
elif num2 >= num1:
    t = num2
elif num3 >= num1:
    t= num3
else:
    print(num3)
print(t)

           
