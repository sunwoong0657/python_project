# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제
## : 마우스로 랜덤한 turtle 스탬프를 찍는 프로그램을 작성해보자.
'''
import turtle as T
import random
# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


# turtleStamp 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    T.hideturtle()  # 거북이 숨기기
    T.goto(x, y)    # (x,y)좌표로 거북이 이동
    T.setheading(random.randint(0, 360))    # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    T.shapesize(random.randint(1, 10))      # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor()                 # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    T.fillcolor(r, g, b)                    # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    T.pencolor(r, g, b)                     # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    T.stamp()                               # 스템프 찍기 명령

def clear_bg(x, y):
    T.clear()

T.title('거북이 도장 찍기')                    # 제목 달기 "거북이 도장 찍기"
T.shape('turtle')                           # 도장 모양을 turtle으로 설정
T.speed(0)                                  # 속도 설정
T.penup()                                   # 펜 들기
T.onscreenclick(turtleStamp, 1)             # 왼쪽 마우스 클릭 시, 스탬프 찍기
T.onscreenclick(clear_bg, 3)
T.mainloop()
'''


## turtle 마우스 이벤트 처리 Mission
## : 오른쪽 마우스 클릭 시 화면이 지워지는 기능을 추가해보자.
## turtle 마우스 이벤트 처리 Mission

'''
import turtle

'''
'''
#<turtle 마우스 이벤트 처리 연습문제를 복사해온 뒤, 기능을 추가해보자.>
'''

## turtle 키보드 이벤트 처리 연습문제

import turtle as T
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# 방향키 위를 눌렀을 때의 핸들링 함수
def up():
    T.setheading(90)           # 가려는 방향에 맞게 방향설정
    r, g, b = randomColor() # 랜덤 색상 r,g,b 가져오기
    T.pencolor(r, g, b)     # 펜 색상 설정
    T.fillcolor(r, g, b)    # 거북이의 색상도 같이 설정
    T.forward(10)           # 10만 큼 이동

# 방향키 아래키를 눌렀을 때의 핸들링 함수
def down():
    T.setheading(270)           # 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()  # 랜덤 색상 r,g,b 가져오기
    T.pencolor(r, g, b)      # 펜 색상 설정
    T.fillcolor(r, g, b)     # 거북이의 색상도 같이 설정
    T.forward(10)  # 10만 큼 이동
#T.onkeypress(up, "Up")                 # up 이벤트 설정
#T.onkeypress(down, "Down")             # down 이벤트 설정
#T.listen()                             # listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

def right():
    T.setheading(0)
    r, g, b = randomColor()
    T.pencolor(r, g, b)
    T.fillcolor(r, g, b)
    T.forward(10)

def left():
    T.setheading(180)
    r, g, b = randomColor()
    T.pencolor(r, g, b)
    T.fillcolor(r, g, b)
    T.forward(10)


def escape():
    T.bye() ## turtle 키보드 이벤트 처리 Mission

def clear_bg():
    T.clear()

T.title("마리오의 별을 훔쳐먹는 거북이")  # 제목 설정 "마리오의 별을 훔쳐먹은 거북이"
T.bgcolor('black')  # 배경색을 검정(black)으로 설정하기
T.shape('turtle')
T.pensize(10)

T.onkeypress(left, "Left")
T.onkeypress(right, "Right")
T.onkeypress(up, "Up")
T.onkeypress(down, "Down")
T.onkeypress(clear_bg, "space")
T.onkeypress(escape, "Escape")

T.listen()

T.mainloop()




