scores=[]
sum=0
over_80=0

for i in range (5):
    scores.append(float(input("성적을 입력하시요: ")))
    sum+=scores[i]

    if scores[i] >= 80:
        over_80+=1

    

avg=sum/5

print("성적 평균은 {:.1f} 입니다." .format(avg))
print("80점 이상 성적을 받은 학생은 %d 명입니다." %over_80)
