class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, seen = 0, set()
        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, (r-l+1))

        return longest        
