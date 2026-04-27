import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        while k > 0:
            x = heapq.heappop(gifts)*(-1)
            heapq.heappush(gifts, (-1)*(math.isqrt(x)))
            k -= 1
        return sum(gifts)*(-1)
        