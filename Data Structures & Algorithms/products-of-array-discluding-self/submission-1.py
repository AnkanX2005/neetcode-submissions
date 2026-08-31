class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [0] * len(nums), [0]*len(nums)
        left_multiplier, right_multiplier = 1, 1

        for i in range(len(nums)):
            j = -i-1
            left[i] = left_multiplier
            right[j] = right_multiplier

            left_multiplier = left_multiplier * nums[i]
            right_multiplier = right_multiplier * nums[j]

        return [l*r for l, r in zip(left, right)]    
