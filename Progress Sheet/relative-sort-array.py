class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        store = defaultdict(lambda: len(arr2))
        for idx, num in enumerate(arr2):
            store[num] = idx
        return sorted(arr1,key=lambda x: (store[x],x))