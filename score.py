def Insert(student):
    name = input('이름 입력 : ')

    if (name not in student) == True:

        kor =  int(input('국어 성적을 입력하세요 : '))
        eng =  int(input('영어 성적을 입력하세요 : '))
        math = int(input('수학 성적을 입력하세요 : '))

        print()
        print('[ 이름 :',name,',','국어 :',kor,',','영어 :',eng,',','수학 :',math,']')
        print()
        print('성적이 입력되었습니다.')

        score = kor+eng+math
        avg = round(score/3, 3)

    else:
        print('입력하신 학생은 이미 존재합니다.')
        return Insert(student)

    student[name] = [kor, eng, math, score, avg]
    person = student[name]
    return student

def View(student):
    print('점수 : [ 국어, 영어, 수학, 총점, 평균 ]')

    for key, value in student.items():
        print(key,':', value)
        
    return student

def Search(student):
    search_name = input('검색할 학생의 이름을 입력해주세요 : ')

    if(search_name in student) == True:
        print('점수 : [ 국어, 영어, 수학, 총점, 평균 ]')
        print(search_name,':' , student.get(search_name),' ')

    else:
        print()
        print('입력하신 이름이 없습니다.')
        print()
        print('1) 다시 검색 2) 초기화면으로 가기')
        num = int(input('번호 입력 : '))
        if num ==1:
            Search(student)
        else:
            main()

    return student

def main():
    student = dict()
    print()
    print("[ 성적처리 프로그램 ]");
    print()

    while True:
        select = int(input("1.입력 2.출력 3.검색 4.종료 \n"))

        if select == 1:
            student = Insert(student)

        elif select ==2:
            student = View(student)

        elif select == 3:
            student = Search(student)

        else:
            print("종료되었습니다.")
            break
main()