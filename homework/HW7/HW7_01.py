from tkinter import *

# 윈도우 창을 생성하고 기본 설정을 합니다.
window = Tk()

# 화면에 그림을 그릴 캔버스 위젯을 생성합니다. 
canvas = Canvas(window, bg="white", width=400, height=300)
canvas.pack()

# 사각형을 그리는 함수입니다. 
def draw_rect():
    canvas.create_rectangle(100, 100, 300, 200)

# 타원을 그리는 함수입니다. (사각형에 내접하게 그려집니다.) 
def draw_oval():
    canvas.create_oval(100, 100, 300, 200)

# 대각선 직선을 그리는 함수입니다.
def draw_line():
    canvas.create_line(100, 100, 300, 200)

# 캔버스에 그려진 모든 객체를 삭제하는 함수입니다. 
def clear_canvas():
    canvas.delete(ALL)

# 하단 버튼들을 한 줄로 묶기 위해 프레임을 생성합니다.
frame = Frame(window)
frame.pack()

# 각 버튼을 만들고, 왼쪽부터 차례대로 프레임 안에 배치합니다.
Button(frame, text="사각형 그리기", command=draw_rect).pack(side=LEFT)
Button(frame, text="타원 그리기", command=draw_oval).pack(side=LEFT)
Button(frame, text="직선 그리기", command=draw_line).pack(side=LEFT)
Button(frame, text="삭제하기", command=clear_canvas).pack(side=LEFT)

# 이벤트 루프를 시작하여 윈도우 창을 유지합니다.
window.mainloop()
