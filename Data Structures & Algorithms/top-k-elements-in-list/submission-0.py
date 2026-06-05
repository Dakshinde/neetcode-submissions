class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            if i not in count_map:
                count_map[i] = 1
            else:
                count_map[i] += 1
        
        def get_freq(z):
            return z[1]

        lala = sorted(count_map.items(),key = get_freq ,reverse = True)

        lis1 = []
        
        for i in lala:
            lis1.append(i[0])
        
        return lis1[:k]
