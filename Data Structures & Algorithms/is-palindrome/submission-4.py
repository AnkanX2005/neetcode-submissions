class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        alphabet_set = set(alphabet)

        l = 0
        r = len(s) - 1


        while l < r:
            while l < r and s[l] not in alphabet_set:
                l += 1
            while r > l and s[r] not in alphabet_set:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True                
