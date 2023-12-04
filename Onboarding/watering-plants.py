class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        full = capacity + 1 - 1
        steps = 0
        for pot in range(len(plants)):
            if plants[pot] > capacity:
                capacity = full
                steps += 2 * pot 
            steps += 1    
            capacity -= plants[pot]
        return steps