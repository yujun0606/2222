score = int(input('점수를 입력하세요'))

 
if score >= 90:
    grade = 'a'
elif score >= 80:
    grade = 'b'
elif score >= 70:
    grade = 'c'
elif score >= 60:
    grade = 'd'
elif score >= 50:
    grade = 'e'
else:
    grade = 'f'

print(f'당신의 학점은 {grade}')

            
            
        
