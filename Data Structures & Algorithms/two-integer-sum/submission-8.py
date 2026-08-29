class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count, answer = {}, []
        for index, num in enumerate(nums):
            count[num] = index

        for i in range(len(nums)):
            need = target - nums[i]
            if need in count and count[need] != i:
                answer.append([i, count[need]])

        return answer[0]            