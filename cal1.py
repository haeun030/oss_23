sum_g = 0 #열람용 f 포함
sum_r = 0 #제출용 f 제외
re = 0
total = 0
total_r = 0
total_g = 0
gpa_r = 0
gpa_g = 0
casef_r= 0
casef_g=0

def choice_1():


    print("학점을 입력하세요")
    unit = int(input())
    print("평점을 입력하세요")
    credit = input()

    global sum_g
    global sum_r  # 전역 변수 사용 선언
    new_sum_g = sum_g + unit # 덧셈 연산 후 결과를 새로운 변수에 할당
    sum_g = new_sum_g
    new_sum_r = sum_r + unit
    sum_r = new_sum_r

    global re
    re += 1


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
            global casef_r
            global casef_g
            score = 0.0
            sum_r = sum_r - unit
            casef_r = score * unit
            return 0
    
def main():
     global total
     global total_r
     global total_g
     global casef_r
     
     print("작업을 선택하세요")
     print("1. 입력 \n2. 계산")
     choice = int(input())  #문자열로 받으니까 꼭 인트로 감싸주거나 아래 1을 따옴표로 감싸줘!!

     if choice == 1:
         total += choice_1() #실행하고 리턴값 바로 저장해줘야함
         total_r = total / float(sum_r)
         total_g = (total + casef_r) / float(sum_g)
         print("입력되었습니다")
         main()
         
     elif choice == 2:
         print("제출용: {}학점 (GPA: {})".format(sum_r, total_r))  ## 포맷 공부해라 하은아!!!!!
         print("열람용: {}학점 (GPA: {})".format(sum_g, total_g))
         print("프로그램을 종료합니다")

main()