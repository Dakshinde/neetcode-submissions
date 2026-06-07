class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]
        right = [1]

        for i in range(1,len(nums)):
            left.append(left[i-1] * nums[i-1])
        print(left)

        for i in range(len(nums)-2,-1,-1):
            right.append(right[-1] * nums[1+i])
        print(right)
        
        right = right[::-1]
        print(right)
        
        result = []
        for i in range(len(left)):
            result.append(left[i] * right[i])
        
        return result