class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {}

        for char in s:
            if char not in seenS:
                seenS[char] = 1
            else:
                seenS[char] += 1

        for char in t:
            if char not in seenT:
                seenT[char] = 1
            else:
                seenT[char] += 1
        
        print(seenS)
        print(seenT)

        for i in seenS:
            if i in seenT:
                if seenS[i] != seenT[i]:
                    return False
            else:
                return False
        
        return True