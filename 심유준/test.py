h = float(input('키 :')) / 100
w = float(input('몸무게 :'))

bmi = w / (h*h)

if bmi >= 40:
    b = '고도 비만'
elif bmi >= 35:
    b = '중증도(2단계) 비만'
elif bmi >= 30:
    b = '경도(1단계) 비만'
elif bmi >= 25:
    b = '과체중'
elif bmi >= 18.5:
    b = '정상'
else:
    b = '저체중'

print('당신의 체질량 지수는 {} 입니다.{}입니다'.format(bmi, b))

    
