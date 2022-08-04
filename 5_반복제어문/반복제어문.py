# for : 특정 횟수를 기반으로 반복, break 문을 만나지 않으면 else: 를 실행하도록 할 수 있다.
# while : 특정 기준을 기반으로 반복

for num in [10, 20, 30]:
    print(num)
    # 리스트 항목이 반복하면서 차례대로 변수 num에 할당된다.

# zip 함수 인수로 넘겨받은 시퀀스들의 n번째 위치한 값들을 튜플로 묶어준다
name = ["A", "B", "C"]
age = ["12", "33", "23"]

for n, a in zip(name, age):
    print(n, a)

print(list(zip(name, age)))

# enumerate : 각각의 요소 앞에 인덱스를 추가
numbers = [44, 55, 11, 23, 43, 12]
key = 23
print(list(enumerate(numbers)))
print(enumerate(numbers))ß
for idx, num in enumerate(numbers):
    if key == num:
        print("{0}의 값은 {1}번째 있습니다.".format(key, idx+1))
