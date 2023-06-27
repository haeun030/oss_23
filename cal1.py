sum_credit_v = 0  # 열람용 총학점 f 포함 view
sum_credit_s = 0  # 제출용 총학점 f 제외 submit
total_gpa = 0
total_v = 0  # gpa 평균 열람용
total_s = 0  # // 제출용
casef_v = 0  # 열람용을 위한 f일 때 이용 변수


def choice_1():
    print("학점을 입력하세요")
    unit = int(input())
    print("평점을 입력하세요")
    credit = input()

    global sum_credit_v
    global sum_credit_s  # 전역 변수 사용 선언

    new_sum_credit_v = sum_credit_v + unit  # 덧셈 연산 후 결과를 새로운 변수에 할당
    sum_credit_v = new_sum_credit_v
    new_sum_credit_s = sum_credit_s + unit
    sum_credit_s = new_sum_credit_s

    match credit:
        case "A+":
            score = 4.5
            return score * unit
        case "A":
            score = 4.0
            return score * unit
        case "B+":
            score = 3.5
            return score * unit
        case "B":
            score = 3.0
            return score * unit
        case "C+":
            score = 2.5
            return score * unit
        case "C":
            score = 2.0
            return score * unit
        case "D+":
            score = 1.5
            return score * unit
        case "D":
            score = 1.0
            return score * unit
        case "F":
            global casef_v
            score = 0.0
            sum_credit_s = sum_credit_s - unit
            casef_v = score * unit
            return 0


def main():
    global total_gpa
    global total_v
    global total_s
    global casef_v

    print("작업을 선택하세요")
    print("1. 입력 \n2. 계산")
    choice = int(input())  # 문자열로 받으니까 꼭 인트로 감싸주거나 아래 1을 따옴표로 감싸줘!!

    if choice == 1:
        total_gpa += choice_1()  # 실행하고 리턴값 바로 저장해줘야함
        total_s = total_gpa / float(sum_credit_s)
        total_v = (total_gpa + casef_v) / float(sum_credit_v)
        print("입력되었습니다")
        main()

    elif choice == 2:
        print("열람용: {}학점 (GPA: {:.2f})".format(sum_credit_v, total_v))  ## 포맷 공부해라 하은아!!!!!
        print("제출용: {}학점 (GPA: {:.2f})".format(sum_credit_s, total_s))  ### :.2f 넣어주면 두 자리까지!!
        print("프로그램을 종료합니다")


main()