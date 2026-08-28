class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        st = [0]


        seen[0] = True
        while st:
            r = st.pop()
            for k in rooms[r]:
                if not seen[k]:
                    st.append(k)
                    seen[k] = True
        for s in seen:
            if not s:
                return False

        return True