
####################### ex 1-1
# number = int(input())
#
# for i in range(2, number+1): #하은아 소괄호와 콤마란다
#
#     if number % i == 0:
#         if number == i:
#             print("소수입니다")
#         else:
#             print("소수가 아닙니다")
#     else:
#         continue

###################### ex 1-2


# def main():
#     import random
#     #real_answer = random.random()## 두 가지는 세트란다
#
#     real_answer= random.randint(0, 100)
#
#     for i in range(1,11):
#         answer = int(input())
#         #i += 1 얘는 왜 없어도 됨 자동으로 1씩 추가해줌!!!
#         if answer == real_answer:
#             print("승리했습니다")
#             return # 함수 종료되도록 써주기!!
#         elif answer > real_answer:
#             print("UP")
#         elif answer < real_answer:
#             print("down")
#     print("실패했습니다")
# main()

####################### ex 1-3

# import random
# first = random.randint(0, 9)
# second = random.randint(0, 9)
# third = random.randint(0, 9)
# strike = 0
# ball = 0
# chance = 0
#
# while first == second or second == third or third == first:
#     first = random.randint(0, 9)
#     second = random.randint(0, 9)
#     third = random.randint(0, 9)
# #겹치지 않게 만드는 코드 생성
#
# real_answer = [first,second,third] ## 자료구조 공부하기
# answer = []
#
# print(real_answer[:])
#
# def main():
#
#     global strike
#     global ball
#     global chance
#     while chance < 11:
#
#         strike = 0
#         ball = 0
#         answer = []  # 이전 입력 값을 제거하기 위해 빈 리스트로 초기화!! 해줘야지
#
#         for i in range(3):
#             # answer[i] = int(input()) ## 이렇게 하면 안 됨. i에 해당하는 요소가 없어서
#             answer.append(int(input()))  # 값 알아서 순서대로 저장 됨
#
#         for i in range(3):
#             if answer[i] in real_answer:
#                 if answer[i] == real_answer[i]:
#                     strike += 1
#                 else:
#                     ball += 1
#             else:
#                 continue
#         chance += 1
#
#         if strike == 3:
#             print("승리했습니다")
#             return
#         else:
#             print('{}스트라이크, {}볼입니다'.format(strike, ball))
#
#
#     if chance == 10:
#         print("실패했습니다")
#         return
#
# main()

#################### ex 1-4

import random
number = int(input())
exponent = random.randint(0,128)

while number < 2 ** exponent or number > 2 **(exponent + 1):
    exponent = random.randint(0,128)
print(exponent)

#two = [exponent+1] 이건 지수 플러스 1을 요소로 갖는 리스트

size = exponent + 1
two= [0] * size

for i in range(0,exponent,2): #간격이 2이려면 2가 맨 뒤여야함
    k = 0
    if i == 0:
        two.insert(k, 3)
    else:
        if (number / i) <= (2 ** i):
            two.insert(k, 1)
        else:
            two.insert(k, 0)
    k += 1

print(two[:])
print(k)

########################































