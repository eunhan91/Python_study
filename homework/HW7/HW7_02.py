import time
from tkinter import *

# 윈도우 창을 생성하고 캔버스를 화면에 추가합니다. 
window = Tk()
canvas = Canvas(window, width=400, height=200)
canvas.pack()

# 화면에 움직일 텍스트를 생성하고, 제어하기 위해 ID를 저장해 둡니다. 
text_id = canvas.create_text(50, 100, text="파이썬 커피샵으로 오세요!")

# 애니메이션 효과를 위해 무한 루프를 돌며 글자를 이동시킵니다.
while True:
    # 지정된 텍스트 객체를 x축 방향으로 3픽셀씩 이동시킵니다. 
    canvas.move(text_id, 3, 0)
    
    # 변경된 위치를 화면에 즉시 반영하기 위해 화면을 업데이트합니다. 
    window.update()
    
    # 글자가 너무 빨리 지나가지 않도록 0.05초 대기합니다. 
    time.sleep(0.05)