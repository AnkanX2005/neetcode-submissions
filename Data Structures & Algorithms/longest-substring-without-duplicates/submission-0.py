class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        se = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            se.add(s[r])
            longest = max(longest, (r-l+1))    
        return longest
        