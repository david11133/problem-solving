def threeSum(nums):
    nums.sort()
    result = set()
 
    for i in range(len(nums) - 2):
        first = nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            second = nums[left]
            third = nums[right]
            current_sum = first + second + third

            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                result.add((first, second, third))
                left += 1
                right -= 1
    return list(result)

res = threeSum([-1, 0, 1, 2, -1, -4])
print(res)
