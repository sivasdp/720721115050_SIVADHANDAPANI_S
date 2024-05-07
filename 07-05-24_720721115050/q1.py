# Answer for q1

def solution(l: list,target: int):
    for i in range(len(l)):
        for j in range(1,len(l)):
            if l[i]+l[j]==target:
                return [i,j]

# Use case 1
nums=[2,7,11,15]
print("Use case 1")
print(solution(l=nums,target=9))

# Use case 2
nums2=[3,2,4]
print("Use Case 2")
print(solution(l=nums2,target=6))

# Use case 3
nums3=[3,3]
print("Use case 3")
print(solution(l=nums3,target=6))