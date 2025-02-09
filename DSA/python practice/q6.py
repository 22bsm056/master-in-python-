nums = [8, 7, 2, 5, 3, 1] 
target = 10
for i in range(len(nums)):
    num=nums[i]
    for j in range(len(nums)):
        if num + nums[j] ==target and i!=j and i<j:
            print(num,nums[j])
        else:
            pass

#chatgpt
nums = [8, 7, 2, 5, 3, 1] 
target = 10
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] ==target:
            print(nums[i],nums[j])

#final leetcode
class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the complement and its index
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i  # Store the index of the current number

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
