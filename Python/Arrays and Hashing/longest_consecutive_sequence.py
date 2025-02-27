def longest_consecutive(nums):

    if not nums:
        return 0
    num_set = set(nums)
    lingest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            lingest_streak = max(lingest_streak, current_streak)
    return lingest_streak

print(longest_consecutive([100, 4, 200, 1, 3, 2])) # 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(longest_consecutive([1,2,0,1])) # 3