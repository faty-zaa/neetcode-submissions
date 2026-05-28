class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hach = {}
        lst = []
        ln = len(nums)
        for i in range(ln):
            diff = target - nums[i]
            if diff in hach:
                if i != hach[diff]:
                    lst.append(hach[diff])
                    lst.append(i)
                    return lst
            hach[nums[i]] = i
        return lst




        