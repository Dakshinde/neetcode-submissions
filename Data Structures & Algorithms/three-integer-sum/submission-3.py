class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        i = 0
        
        nums = sorted(nums)
        print(nums)
        

        for i in range(len(nums)):
            k = len(nums) - 1
            j = i + 1

            #print(f"i j k are {i,j,k}")

            if i > 0 and nums[i] == nums[i-1]:
                continue 

            while j < k:
                
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    result.append([nums[i], nums[j] , nums[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1     
                elif current_sum < 0:
                    j = j + 1
                elif current_sum > 0:
                    k = k - 1  
                # print(f"i j k are {i,j,k}")
            
        
        return result # O(N^2) time and O(1)or O(N) space 
        