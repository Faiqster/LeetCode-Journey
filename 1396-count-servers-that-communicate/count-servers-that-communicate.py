class Solution(object):
    def countServers(self, grid):
        row = len(grid)
        col = len(grid[0])
        server_positions = set() 
        for i in range(row):
            row_positions = []
            for j in range(col):
                if grid[i][j] == 1:
                    row_positions.append((i, j))  
            if len(row_positions) > 1:
                server_positions.update(row_positions)

        for j in range(col):
            col_positions = []
            for i in range(row):
              if grid[i][j] == 1:
                col_positions.append((i, j))
            if len(col_positions) > 1:
                server_positions.update(col_positions)
        return len(server_positions)