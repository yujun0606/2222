## 1부터 10까지 합을 구함 : 55
# 1) for문
# 2)while문
'''s = 0

for x in range(1, 11):
    s = s + x
    print(f'sum : {s}')'''
    
'''sum = 0
x = 1
while x <= 10:
    sum = sum + x
    x = x + 1
print(f'sum : {sum}')'''
sum = 0
i = 1
while i <= 10:
    i = i + 1
    if i % 2 == 0:
        sum = sum + i
    
    

print(sum)
# 2 4 6 8 10

    



