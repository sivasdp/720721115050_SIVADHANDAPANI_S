# A function to find the longest common prefix string ammong given array

def solution(strs: list):
    a=strs[0]
    for i in range(1,len(strs)):
        while strs[i].find(a)!=0:
            a=a[:-1]
    return a

# Use case 1
print("Usecase 1:")
strs=["flowers","flow","flight"]
print(solution(strs))

#Use case 2:
print("Use case 2:")
strs2=["dog","racecar","car"]
print(solution(strs2))
