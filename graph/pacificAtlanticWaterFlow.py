from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Pacific
        q = deque()
        for i in range(len(heights)):
            q.append((i, 0))
        for i in range(1, len(heights[0])):
            q.append((0, i))
        toPacific = set()

        while q:
            pos = q.popleft()
            if pos in toPacific:
                continue
            else:
                toPacific.add(pos)
            r, c = pos[0], pos[1]
            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                q.append((r-1, c))
            if r + 1 < len(heights) and heights[r+1][c] >= heights[r][c]:
                q.append((r+1, c))
            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                q.append((r, c-1))
            if c + 1 < len(heights[0]) and heights[r][c+1] >= heights[r][c]:
                q.append((r, c+1))
        
        # Atlantic
        q.clear()
        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
        for i in range(0, len(heights[0])-1):
            q.append((len(heights)-1, i))
        toAtlantic = set()
        while q:
            pos = q.popleft()
            if pos in toAtlantic:
                continue
            else:
                toAtlantic.add(pos)
            r, c = pos[0], pos[1]
            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                q.append((r-1, c))
            if r + 1 < len(heights) and heights[r+1][c] >= heights[r][c]:
                q.append((r+1, c))
            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                q.append((r, c-1))
            if c + 1 < len(heights[0]) and heights[r][c+1] >= heights[r][c]:
                q.append((r, c+1))
        
        rv = []
        for pair in toPacific:
            if pair in toAtlantic:
                rv.append([pair[0], pair[1]])
        return rv
