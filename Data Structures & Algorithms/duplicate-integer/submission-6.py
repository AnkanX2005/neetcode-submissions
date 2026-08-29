class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        return True if max(count.values())>1 else False