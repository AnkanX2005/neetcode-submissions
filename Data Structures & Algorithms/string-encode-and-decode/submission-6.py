class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'ankan'
        result = '!-'.join(strs)
        return result    

    def decode(self, s: str) -> List[str]:
        if s == 'ankan':
            return []
        x = s.split('!-')
        return x    
