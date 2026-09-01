class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        # O(n * k) 
        # Before I used sorted function to group key => O(klog(k))
        # Now I don't need sorted with grouping key by tuple(list)

        seen = {}
        for str in strs:
            count = [0] * 26 # 26 alphabet
            for char in str:
                count[ord(char) - ord('a')] += 1 # act => [1, 0, 1, 0,..., 1,...]
            
            tempTuple = tuple(count) # Only immutable data structure can be used as key
            if seen.get(tempTuple, 0) != 0:
                seen[tempTuple].append(str)
            else:
                seen[tempTuple] = [str]
        
        return list(seen.values())
        