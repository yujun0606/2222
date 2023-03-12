# continue문
'''
continue 아래쪽 문장을 건너뜨;거 계속해서 for, while문 실행 
'''
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)

print('-----------------')

#break문
'''
break를 만나는 순간 for, while 문은 종료
'''
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        break
    print(i)
