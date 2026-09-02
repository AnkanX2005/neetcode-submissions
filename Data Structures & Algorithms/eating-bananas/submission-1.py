import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximun_eating_rate = max(piles)

        l = 1
        r = maximun_eating_rate

        ans = r

        while l <= r:
            k = (l+r) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                ans = k
                r = k-1
            else:
                l = k + 1

        return ans                