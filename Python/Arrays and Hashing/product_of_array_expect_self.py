def productExpectSelf(lst):
    n = len(lst)
    result = [1] * n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= lst[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= lst[i]

    return result


print(productExpectSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExpectSelf([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]