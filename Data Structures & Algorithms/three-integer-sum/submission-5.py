class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for i, num in enumerate(nums):
            count[num] = i

        result = set()    

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                desired = 0 - (nums[i] + nums[j])
                if desired in count and (count[desired] != i and count[desired]!=j):
                    result.add(tuple(sorted((desired, nums[i], nums[j]))))

        return list(result) 