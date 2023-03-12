# 6316. Rearrange Array to Maximize Prefix Score
'''
nums = [2,-1,0,1,-3,3,-3]

objective: rearrange nums in whatever order the user determines: nums = [...]

constraints:
1 <= nums.length <= 105
-106 <= nums[i] <= 106
'''


def prefix(nums, i):
    '''
    nums: array of ints
    i: int

    return: sum of the first i-th elements in the nums
    '''
    counter = 0
    for integer in nums[:i + 1]:
        if integer > 0:
            counter += integer
    return counter


nums = [2,-1,0,1,-3,3,-3]
nums = [2, -1, 1]

def rearrange(nums):
    new_list = []
    for i in nums:
        if i > 0:
            new_list.append(i)
    return new_list

print(rearrange(nums))

def prefix(nums):
    # i-th element is the sume of the (i + (i- 1))-th element
    new_list = []
    for i in range(len(nums)):
        if i == 0:
            new_list.append(nums[i])
        elif i > 0:
            new_list.append(nums[i] + nums[i - 1])
    return new_list

def maximum_element(nums):
    return max(nums)


print(max(prefix(rearrange(nums))))


def sum_of_nums(nums):
    total_sum = 0
    for i in nums:
        total_sum += i
    return total_sum

print(sum_of_nums(nums))