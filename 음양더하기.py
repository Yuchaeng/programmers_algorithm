def solution(absolutes, signs):
    num=[]
    for i in range(len(absolutes)):
        num.append(0)
    for i in range(len(absolutes)):
        if signs[i]==True:
            num[i]=absolutes[i]
        else:
            num[i]=-absolutes[i]
    return sum(num)

#zip 함수 사용
def solution(absolutes, signs):
    sum=0
    for i,j in zip(absolutes, signs):
        if j:
            sum+=i
        else:
            sum+=-i
    return sum