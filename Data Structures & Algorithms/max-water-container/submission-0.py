class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0 
        j = len(heights) - 1

        while i < j:
            print(i,j)
            print(heights[i], heights[j])
            current_area = min(heights[i],heights[j]) * abs(i-j) 
            # area = area = min(i,j) * mod(i-j) mathematically saying mod means mod(-1) = 1 
            print(current_area)

            if current_area > area :
                area = current_area
                
            if heights[i] < heights[j]:
                i = i + 1
            
            else:
                j = j - 1
                
        return area