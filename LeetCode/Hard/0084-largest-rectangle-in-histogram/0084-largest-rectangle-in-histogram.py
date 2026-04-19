class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area= 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                prev_height = heights[stack.pop()]
                
                if not stack:
                    w = i
                else:
                    w = i-stack[-1]-1

                max_area = max(max_area, prev_height * w)

            stack.append(i)

        return max_area
