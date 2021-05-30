def div(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count

def solution(left, right):
    sum=0
#제곱->약수 홀수 이용
#int(math.sqrt(i))==math.sqrt(i) 면 제곱수
    for i in range(left, right+1):
        if div(i)%2==0:
            sum+=i
        else:
            sum-=i
    return sum
