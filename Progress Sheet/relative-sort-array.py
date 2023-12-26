class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        uniques = []
        set2 = set(arr2)
        for num in arr1:
            if num not in set2:
                uniques.append(num)
        uniques.sort()
        for num in arr2:
            res += [num] * freq[num]
        return res + uniques