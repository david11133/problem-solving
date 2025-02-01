def productExpectSelf(lst):

  n = len(lst)
  result = [1] * n

  prefix = 1
  for i in range(n):
    result[i] = prefix
    prefix *= lst[i]

  suffix = 1
  for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= lst[i]

  return result
