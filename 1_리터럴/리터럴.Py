# 리터럴 값 그 자체를 의미함

# 1. 정수 리터럴
# 10진수 그냥 숫자 입력
# 16진수 숫자 앞에 0x
# 8진수 숫자 앞에 0o
# 2진수 숫자 앞에 0b
# int('표현값',사용할 진수)
# 입력은 다음과 같이 해도 기본 default 출력값은 10진수로 출력됨. 다른 진수로 출력을 원할 경우 format 나타내는 문법이용해야함 bin(값) oct(값) hex(값)

print(137)

print(0x137)

print(0o137)

print(int('11', 4))

print(0b10010011)


# 실수 리터럴(소수점 및 지수 의미)
print(1e10)
print(3.14e-10)
print(0e0)

# 허수 표현시 j 써주면 된다
print(3.14j)


# 문자 리터럴 양끝에 "" or '' 이용
print(type(123))
print(type("123"))
print(type('123'))

# escape 시퀀스 이용 \
