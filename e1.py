class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}

        # print(7 in d)

        for i, x in enumerate(nums):
            print(target-x)
            if (target-x) in d:
                return [d[target-x], i]
            else:
                d[x] = i
            # print(d)       
x = Solution()
print(x.twoSum([2,7,11,15], 9))
print(x.twoSum([3,2,4], 6))
print(x.twoSum([3,3], 6))

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6

