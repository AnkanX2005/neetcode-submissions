
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # s_count = Counter(s)
        # t_count = Counter(t)

        # if s_count == t_count:
        #     return True
        # else:
        #     return False    

        # return sorted(s) == sorted(t)

        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT    
