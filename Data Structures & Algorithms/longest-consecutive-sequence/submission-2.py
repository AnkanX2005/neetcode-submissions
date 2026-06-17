class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seT = set(nums)
        seq = 0

        for num in seT:
            if (num-1) not in seT:
                length = 1
                while (num + length) in seT:
                    length += 1
                seq = max(length, seq)
        return seq            
  
        