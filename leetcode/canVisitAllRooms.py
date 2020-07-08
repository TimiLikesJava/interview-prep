class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        array = [False] * len(rooms)
        array[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if array[i] != True:
                    array[i] = True
                    stack.append(i)
        return all(array)
