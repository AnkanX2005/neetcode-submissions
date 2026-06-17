class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            strs = sorted(i)
            sortedS = ''.join(strs)
            result[sortedS].append(i)

        return list(result.values())    

        
        