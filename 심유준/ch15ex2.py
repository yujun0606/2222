# ch15ex2.py
# 2023.02.22 김준형
# 문구점 제고 관리하기
product = {}  # 빈 사전 생성

# 재고 사전 만들기
##while True:
##    name = input('재고 품목을 입력하세요(입력의 끝은 "끝"입력)')
##    # key = name
##    if name == '끝':
##        break
##
##    cnt = int(input('재고 개수는?')) # value : cnt
##    
##    # 사전에 추가
##    product[name] = cnt

product = {'노트': 3, '볼펜': 7, '지우개': 5}

# 딕셔너리 값 출력
# 지우개의 재고개수 출력하기
print('지우개:', product['지우개'])

# 노트의 재고개수 4로 변경
product['노트'] = 4
print(product)
