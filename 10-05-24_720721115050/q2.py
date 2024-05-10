# Solution for q2

def Solution(num: list):
    ans=0
    for i in num:
        ans^=i
    return ans

#Usecase 1:
print("Use case 1:")
nums1=[2,2,1]
print(Solution(nums1))

#Usecase 2:
print("Use case 2:")
nums2=[4,1,2,1,2]
print(Solution(nums2))

#Usecase 3:
print("Use case 3:")
nums3=[1]
print(Solution(nums3))
