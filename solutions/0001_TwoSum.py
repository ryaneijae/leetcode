class Solution:
    def sort_ans(self, i, j):
        if i > j:
            return [j, i]
        return [i, j]
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        checked = {}
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in checked:
                return self.sort_ans(i, checked[looking_for])
            else:
                checked[nums[i]] = i
