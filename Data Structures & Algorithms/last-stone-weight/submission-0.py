import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [i*(-1) for i in stones]
        heapq.heapify(new_stones)
        while(len(new_stones) > 1):
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(new_stones, x - y)
            else:
                heapq.heappush(new_stones, y - x)
        
        if (len(new_stones)):
            return new_stones[0]*(-1)
        return 0
        
        