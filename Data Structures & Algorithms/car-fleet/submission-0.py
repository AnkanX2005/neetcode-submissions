class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []

        for i in range(len(cars)-1, -1, -1):
            pos, spe = cars[i]
            time = (target - pos) / spe

            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)        
        