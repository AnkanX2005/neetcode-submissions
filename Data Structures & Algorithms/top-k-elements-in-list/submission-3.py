class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        dict_arr = []
        for key, val in count.items():
            dict_arr.append((val, key))

        dict_arr.sort()
        answer = []
        for i in range(k):
            val, key = dict_arr.pop(-1)
            answer.append(key)

        return answer        

