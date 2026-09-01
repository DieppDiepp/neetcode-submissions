class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        # O(n * klog(k)) 
        
        sortList = [''.join(sorted(s)) for s in strs]
        
        seen = {}
        for i in range(0, len(sortList)):
            if seen.get(sortList[i], 0) == 0:
                seen[sortList[i]] = [strs[i]]
            else:
                seen[sortList[i]].append(strs[i])

        # print(seen)

        output = []
        for value in seen.values():
            output.extend([value])

        return output

       
