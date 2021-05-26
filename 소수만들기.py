import itertools
def prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
        return True
    else:
        return False

def solution(nums):
    result=0
    com=list(itertools.combinations(nums,3))
    for i in range(len(com)):
        if prime(sum(com[i]))==True:
            result+=1
    return result