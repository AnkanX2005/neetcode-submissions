class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        start = []

        for num in nums:
            if num-1 not in seen:
                start.append(num)
        sequence = 0
        longest = 0
        i = 0
        while i < len(start):
            num = start[i]
            while num in seen:
                sequence += 1
                num = num+1
            longest = max(longest, sequence)    
            i += 1
            sequence = 0
        return longest    
                