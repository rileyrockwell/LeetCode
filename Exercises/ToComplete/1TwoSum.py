class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_copy = nums
        list_without_ith = []
        result = []
        for i in nums_copy:
            # for j in nums_copy.remove from the i-th index from nums_copy
            if i + j == target:
                result.append(i)
                result.append(j)
                # result.append(i, j)

if __name__ == "__main__":
    print(Solution().twoSum([0, 1, 2, 3, 4, 5, 6], 10))