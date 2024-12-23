class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_ind = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_ind:
                return [num_to_ind[compliment], i]
            num_to_ind[num] = i

            
numeros = [2,5,4,11]
targeto = 6

function = Solution()
result = function.twoSum(numeros, targeto)

print(result)

