import tkinter as tk

# 1. 메인 창 생성 및 타이틀 설정
root = tk.Tk()
root.title("tk")

# 이미지에 표시된 색상 이름 리스트 정의
colors = ["green", "red", "orange", "white", "yellow", "blue"]

# 2. 색상의 개수만큼 반복하면서 레이블과 버튼 생성 및 격자(grid) 배치
for i, color in enumerate(colors):
    # 왼쪽 열(column=0): 색상 이름이 들어간 레이블
    # width와 relief를 설정하여 이미지처럼 일정한 크기와 테두리를 갖도록 합니다.
    label = tk.Label(root, text=color, width=15, height=2, relief="groove", bd=1)
    label.grid(row=i, column=0, sticky="nsew")
    
    # 오른쪽 열(column=1): 해당 색상이 적용된 버튼
    # bg(background)로 배경색을 지정합니다.
    button = tk.Button(root, bg=color, width=10, height=2, relief="raised")
    button.grid(row=i, column=1, sticky="nsew")

# 3. 창이 닫히기 전까지 이벤트 루프 실행
root.mainloop()