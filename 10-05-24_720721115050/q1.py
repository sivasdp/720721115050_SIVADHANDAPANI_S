# Solution for q1

def solution(n: int):
    a,b,c=0,1,0
    for i in range(n):
        c=a+b
        a=b
        b=c
    return b

#Use case 1:
print("Use case 1:")
print(solution(n=2))


#Use case 2:
print("Use case 2:")
print(solution(n=3))