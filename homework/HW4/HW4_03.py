import random

# 10x10 보드 초기화 (전부 '.'으로 세팅)
board = [['.' for j in range(10)] for i in range(10)]

# 지뢰 매설
for i in range(10):
    for j in range(10):
        # 30% 확률로 해당 좌표에 지뢰(#) 할당
        if random.random() < 0.3:
            board[i][j] = "#"

# 보드 출력
for i in range(10):
    for j in range(10):
        print(board[i][j], end=" ")
    print()  # 개행