class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        area = 0
        i = 0 
        j = len(height) - 1

        left_max = height[i]
        right_max = height[j]

        while i < j :
            
            if left_max < right_max :
                i = i + 1
                left_max = max(left_max, height[i])
                area = area + (left_max - height[i])
            else:
                j = j - 1
                right_max = max(right_max,height[j])
                area = area + (right_max - height[j])
                

        return area