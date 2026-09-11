class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):


            while stack and stack[-1][1] < temperatures[i]:
                answer[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperatures[i]))

        return answer    
            