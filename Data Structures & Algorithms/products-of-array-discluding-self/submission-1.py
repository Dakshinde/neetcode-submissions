class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]
        right_val = 1

        for i in range(1,len(nums)):
            result.append(result[i-1] * nums[i-1])
        print(result)

        for i in range(len(nums)-1,-1,-1):
            print(result[i])
            result[i] = result[i] * right_val
            right_val = right_val * nums[i]
            print(f"Right variable is :{right_val}")
    
        
        return result