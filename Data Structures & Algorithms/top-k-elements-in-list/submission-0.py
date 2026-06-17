class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True ))
        arr = []
        key_list =  list(sorted_dict.keys())
        i = 0
        while i < k:
            arr.append(key_list[i])
            i += 1
        return (sorted(arr))    