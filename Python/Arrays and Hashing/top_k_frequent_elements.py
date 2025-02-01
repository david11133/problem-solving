class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        sorted_dict = sorted(nums_dict.items(), key=operator.itemgetter(1), reverse=True)
        result = [item[0] for item in sorted_dict[:k]]
        return result
