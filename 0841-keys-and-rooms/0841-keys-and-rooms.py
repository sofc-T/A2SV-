class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        keys = deque(rooms[0])

        while keys:
            key = keys.pop()
            if key not in visited:
                visited.add(key)
                keys.extendleft(rooms[key])


        return len(visited) == len(rooms)
        