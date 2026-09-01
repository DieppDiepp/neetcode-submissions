class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min Loop -> O (n * k)
        # Sort -> O(nlogn)
        # Heap -> O(n + k*logn)

        # Min Loop
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        # print(f"cnt {cnt}")
        
        topK = []

        for _ in range(k):
            maxV = float('-inf')
            maxK = None

            for key, val in cnt.items():
                if val > maxV and key not in topK:
                    maxV = val
                    maxK = key
            # print(f"maxK = {maxK}, maxV = {maxV}")

            if maxK is not None:
                topK.append(maxK)
        
        return topK



        