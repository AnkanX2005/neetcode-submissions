class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for words in strs:
            sorted_word_list = sorted(words)
            sorted_word = ''.join(sorted_word_list)
            result[sorted_word].append(words)

        return list(result.values())    