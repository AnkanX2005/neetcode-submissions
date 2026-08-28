class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = ((0-points[i][0])**2 + (0-points[i][1])**2)
            heapq.heappush(heap,(distance,points[i]))

        answer = []
        for i in range(k):
            distance, pair = heapq.heappop(heap)
            answer.append(pair)

        return answer    