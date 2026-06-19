class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        s = set()

        for i, num in enumerate(nums):
            dic[num] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                desired = -nums[i]-nums[j]
                if desired in dic and dic[desired] != i and dic[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))
        return list(s)            