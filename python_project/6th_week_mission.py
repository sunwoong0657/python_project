# 6주차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[5주차 복습]
1. 연산자(2): 관계, 논리, 멤버십 연산자
2. 입력과 자료형 변환
3. 조건문 if
'''

# 5주차 잘못 업로드 되었던 주제: 논리연산자/ 멤버십 연산자
## 논리연산: and, or, not 연산, 결과는 True or False
## 논리연산 연습문제>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10)       
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야!")
print(not 5==5)
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## 멤버십연산 연습문제>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print("a" in "apple")            
print("d" in "banana")             
print("L" not in "LOSTARK")
'''

# if 조건문 Mission(5주차 이어서)
## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자


## mission4>> Up-down 게임 만들기
## random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기


# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기


## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.


## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자


## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
'''
print("-데이터 수정")
youtuber[6] = '녹두로'
print(youtuber)
'''

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.


## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.


## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자


## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자


## 리스트 mission1
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))


## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다
pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자

## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자

## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자

## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬


#  반복문
## 반복문이란?: 반복적인 작업을 컴퓨터에 시키기 위한 명령.
## 종류: for문(횟수, 시퀀스 자료형), while문(조건)
## 시퀀스 자료형이란?: "순서"가 있는 자료형 (리스트, 문자열, range객체, 튜블, 딕셔너리)

## range() 함수 연습문제: range()를 활용하여
# 여러 활용 해보기 & list로 만들어 결과 확인하기


## for 반복문
## : "횟수 or 시퀀스 자료"에 대한 반복문
## [문법] for 변수 in 시퀀스자료:
##           반복할 문장
## for문 연습문제1: range()를 활용한 "횟수" 반복. 원하는 문자열을 10번 반복해서 출력해보자.


## for문 연습문제2: list를 활용하여 for 반복문 실행시켜 보기


## 이중 for문 연습문제: 이중 for문을 활용하여 높이5의 직각삼각형 만들기


## while 반복문
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용


## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자


## while문 + continue 연습문제


## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기


## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기


## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자


## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.


## 반복문 mission3: 영단어 타자연습 프로그램
# -Learning English-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.

