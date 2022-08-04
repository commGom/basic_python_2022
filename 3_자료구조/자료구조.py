# 리스트 [] : 삭제 가능, 튜플 () : 삭제 불가능, range(시작값,끝값다음값,증분) : 특정 범위의 정수를 나열하는 불변의 시퀀스
k_food = []
j_food = []
c_food = []
food = [k_food, j_food, c_food]

# 추가 append 메서드
k_food.append('라면')
j_food.append('초밥')
c_food.append('자장면')

# 삭제 del food[인덱스] or food.pop(인덱스)

# remove('값')

# 삽입 food.insert(인덱스,값)


# 딕셔너리 : 키와 값이 쌍으로 이루어진 자료형
# {}

memberAge = {"철수": 30, "미희": 20}
print(memberAge["철수"])

# 변경 및 추가 딕셔너리[키]=변경및추가할 값
memberAge["현우"] = 31

print(memberAge)
