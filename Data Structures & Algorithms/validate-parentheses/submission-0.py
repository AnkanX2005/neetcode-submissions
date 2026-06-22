class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != parenthesis[ch]:
                    return False
        return len(stack) == 0                    

        

  
     
    

        