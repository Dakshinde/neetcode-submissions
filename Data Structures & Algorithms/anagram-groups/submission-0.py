class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # key is keys and value is word

        for word in strs:
            keys = "".join(sorted(word))
            print(keys)

            if keys not in groups:
                groups[keys] = []
            
            groups[keys].append(word) #{'aet': ['eat', 'tea']}
        
        return list(groups.values()) # this converts the dictionary to list[list]