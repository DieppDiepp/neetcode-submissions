class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

       
