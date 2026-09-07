class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def count(string):
            count = {}
            
            for s in string:
                count[s] = 1 + count.get(s, 0)
            return count


        l = 0
        r = len(s1)

        while r <= len(s2):
            if count(s1) == count(s2[l:r]):
                return True
            l += 1
            r += 1
        return False    