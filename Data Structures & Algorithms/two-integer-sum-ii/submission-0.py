class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}
        for index, number in enumerate(numbers):
            count[number] = index

        answer = []
        for i in range(len(numbers)):
            desired = target - numbers[i]
            if desired in count and count[desired] != i:
                answer.append([i+1, count[desired]+1])    

        return answer[0]        