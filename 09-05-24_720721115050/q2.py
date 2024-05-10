# Solution for Q2

def Solution(nums: list,target: int):
    if target not in nums:
        nums.append(target)
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==target:
            return i

#Use case 1:
print("Use Case 1:")
nums=[1,3,5,6]
target=5
print(Solution(nums,target))

#Use case 2:
print("Use Case 2:")
nums2=[1,3,5,6]
target2=2
print(Solution(nums2,target2))

#Use case 3:
print("Use Case 3:")
nums3=[1,3,5,6]
target3=7
print(Solution(nums3,target3))