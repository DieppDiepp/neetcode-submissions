class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for id, num in enumerate(nums):
            key = target - num
            if key in map:
                return [id, map[key]] if id < map[key] else [map[key], id]
            else:
                map[num] = id