import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h_m = {}
        for t in tasks:
            if t in h_m:
                h_m[t] += 1
            else:
                h_m[t] = 1
        heap = []
        for k in h_m:
            heap.append(-h_m[k])
        heapq.heapify(heap)
        q = deque()
        c = 0
        while heap or q:
            c += 1
            if heap:
                task = 1 + heapq.heappop(heap)
                if task:
                    q.append([task, c + n])
            if q and q[0][1] == c:
                    heapq.heappush(heap, q.popleft()[0])
        return c

        