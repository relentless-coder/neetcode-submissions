class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i, j = 0, len(heights) - 1
        while i < j:
            if heights[i] <= heights[j]:
                smaller_con = i
            else:
                smaller_con = j
            max_water = max(heights[smaller_con] * (j - i), max_water)
            if smaller_con == i:
                i += 1
            else:
                j -= 1
        return max_water