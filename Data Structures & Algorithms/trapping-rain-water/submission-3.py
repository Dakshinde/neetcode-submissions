class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        maxLeft = [0] * len(height) 
        # creates array of 0s but len of heights so we can append max height for each index
        current_max = 0 # used to compare and append

        maxRight = [0] * len(height)

        i = 0
        j = len(height) - 1

        for i in range(len(height)):
            if height[i] > current_max:
                current_max = height[i]
            maxLeft[i] = current_max
        print(maxLeft)

        current_max = 0 

        while j >= 0:
            if height[j] > current_max:
                current_max = height[j]
            maxRight[j] = current_max
            j = j - 1
        
        print(maxRight)

        for i in range(len(height)):
            current_area = min(maxLeft[i],maxRight[i]) - height[i]
            area = area + current_area
            
        
        return area
             