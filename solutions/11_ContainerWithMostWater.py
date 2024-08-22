class Solution:
    def maxArea(self, height: List[int]) -> int:
        f = 0
        b = len(height) - 1
        maximum = 0
        while f < b:
            maximum = max(maximum, (b - f) * min(height[f], height[b]))
            if height[f] > height[b]:
                b += -1
            else:
                f += 1
        return maximum

    def maxArea_Oofn2(self, height: List[int]) -> int:
        maximum = 0
        for i, h in enumerate(height):
            for j in range(i + 1, len(height)):
                maximum = max(maximum, (j - i) * min(h, height[j]))
        
        return maximum
