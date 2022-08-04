
# 변수 자료가 든 위치(주소) 값을 가지고 있음 : 한 번에 하나의 값을 저장할 수 있는 공간 또는 값 자체를 의미

# 자료형 타입 함수 : type()
# 기억 -> 나누기 연산자를 사용한 결과는 항상 float으로 나옴
# 대입연산자가 가장 후 순위이다.

# 문자열 인덱싱 : 문자열 안에 있는 문자하나에 접근 0부터 시작
# 슬라이싱 : 문자열 일부분을 가져 올 수 있다 [A:B] A부터 B바로 전 까지

# format 메서드
birth = "921129"
year = birth[:2]
month = birth[2:4]
date = birth[4:]

f_string = "19{0}년 {1}월 {2}일"

print(f_string.format(year, month, date))
