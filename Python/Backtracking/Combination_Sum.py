def combinationSum(candidates, target):
    result = []

    def backtrack(start, target, combination_list):
        if target == 0:
            result.append(list(combination_list))
            return 

        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            combination_list.append(candidates[i])
            backtrack(i, target - candidates[i], combination_list)
            combination_list.pop()

    backtrack(0, target, [])
    return result

print(combinationSum([2, 3, 6, 7], 7)) # [[2, 2, 3], [7]]
print(combinationSum([2, 3, 5], 8)) # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]