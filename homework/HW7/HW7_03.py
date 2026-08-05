from tkinter import *

# 윈도우 창을 생성합니다.
window = Tk()

# 입력창 옆에 표시할 텍스트 레이블을 만들고 1열(column=0)에 배치합니다. 
Label(window, text="이름").grid(row=0, column=0, sticky=W, pady=5)
Label(window, text="직업").grid(row=1, column=0, sticky=W, pady=5)
Label(window, text="국적").grid(row=2, column=0, sticky=W, pady=5)

# 사용자가 텍스트를 입력할 수 있는 엔트리 위젯을 생성합니다.
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

# 생성한 엔트리들을 2열(column=1)에 차례대로 배치합니다. 
e1.grid(row=0, column=1, pady=5)
e2.grid(row=1, column=1, pady=5)
e3.grid(row=2, column=1, pady=5)

# Show 버튼을 눌렀을 때 실행되며, 엔트리에 입력된 값을 터미널에 출력합니다. 
def show():
    print("이름: %s\n직업: %s\n국적: %s" % (e1.get(), e2.get(), e3.get()))

# Quit 버튼을 눌렀을 때 실행되며, 프로그램 창을 파괴(종료)합니다. 
def quit():
    window.destroy()

# 맨 아랫줄(row=3)에 Show 버튼과 Quit 버튼을 나란히 왼쪽 정렬로 배치합니다. 
Button(window, text="Show", command=show).grid(row=3, column=0, sticky=W, pady=5)
Button(window, text="Quit", command=quit).grid(row=3, column=1, sticky=W, pady=5)

# 프로그램이 바로 종료되지 않도록 이벤트 루프를 켭니다.
window.mainloop()