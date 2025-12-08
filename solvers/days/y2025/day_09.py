class Day09Solver:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.coordinates = self._parse_input()

    def _parse_input(self):
        coords = []
        for line in self.input_data.split('\n'):
            if ',' in line:
                x, y = map(int, line.strip().split(','))
                coords.append((x, y))
        return coords

    def part1(self) -> "str | int":
        coords = self.coordinates
        max_area = 0
        n = len(coords)
        
        # Check all pairs
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                
                width = abs(x1 - x2) + 1
                height = abs(y1 - y2) + 1
                area = width * height
                
                if area > max_area:
                    max_area = area
                    
        return max_area

    def part2(self) -> "str | int":
        original_coords = self.coordinates
        if not original_coords:
            return 0
            
        # 1. Coordinate Compression
        xs = sorted(list(set(c[0] for c in original_coords)))
        ys = sorted(list(set(c[1] for c in original_coords)))
        
        x_map = {x: i * 2 for i, x in enumerate(xs)}
        y_map = {y: i * 2 for i, y in enumerate(ys)}
        
        # Grid dimensions: 2 * num_unique - 1 possible slots (points and intervals)
        # Add padding for flood fill
        W = len(xs) * 2 + 1
        H = len(ys) * 2 + 1
        
        # 0: Unknown (starts as inside/outside candidate), 1: Boundary/Valid, 2: Outside
        grid = [[0] * W for _ in range(H)]
        
        # 2. Draw Boundary
        n_coords = len(original_coords)
        for i in range(n_coords):
            curr = original_coords[i]
            next_p = original_coords[(i + 1) % n_coords]
            
            x1, y1 = curr
            x2, y2 = next_p
            
            cx1, cy1 = x_map[x1], y_map[y1]
            cx2, cy2 = x_map[x2], y_map[y2]
            
            # Draw line on compressed grid
            # Both are even indices.
            if cx1 == cx2: # Vertical
                r_start, r_end = min(cy1, cy2), max(cy1, cy2)
                for r in range(r_start, r_end + 1):
                    grid[r][cx1] = 1 # Boundary
            else: # Horizontal
                c_start, c_end = min(cx1, cx2), max(cx1, cx2)
                for c in range(c_start, c_end + 1):
                    grid[cy1][c] = 1 # Boundary
                    
        # 3. Flood Fill Outside
        # Start from (0,0) which is guaranteed outside due to mapping logic usually,
        # but let's be safe. Our mapping puts min X at index 0 (grid index 0).
        # We need padding *around* it to ensure flow.
        # Actually our W/H are based on 2*len(xs).
        # xs[0] maps to 0. So grid index 0 is on the edge of the compressed bounding box.
        # Is it possible the bounding box IS the polygon?
        # Safe strategy: Pad the grid by adding virtual extra coords?
        # Or just flood fill from "known outside".
        # If min_x in input is > min possible, we're fine.
        # But we normalized to 0.
        # Let's pad the grid by 1 on all sides for the flood fill.
        
        padded_H = H + 2
        padded_W = W + 2
        # Copy to padded grid (offset by 1)
        # 0: Potential Inside, 1: Wall/Boundary
        p_grid = [[0] * padded_W for _ in range(padded_H)]
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    p_grid[r+1][c+1] = 1
                    
        # Flood fill from (0,0) in padded grid - guaranteed outside
        from collections import deque
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        p_grid[0][0] = 2 # 2 = Outside
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < padded_H and 0 <= nc < padded_W:
                    if (nr, nc) not in visited:
                        if p_grid[nr][nc] != 1: # Not a wall
                            p_grid[nr][nc] = 2 # Mark outside
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            
        # Transfer back validity info
        # 'Bad' map: 1 if Outside (2 in p_grid), 0 if Inside/Boundary (1 or 0 in p_grid)
        # Actually, problem requires "Red or Green".
        # "Inside" (0 in p_grid, which wasn't reached) is Green.
        # "Boundary" (1 in p_grid) is Red/Green.
        # "Outside" (2 in p_grid) is Invalid.
        
        bad_grid = [[0] * W for _ in range(H)]
        for r in range(H):
            for c in range(W):
                if p_grid[r+1][c+1] == 2:
                    bad_grid[r][c] = 1
                    
        # 4. Prefix Sum for Bad Grid
        # S[r][c] = sum(bad_grid[0..r][0..c])
        # Pad prefix array by 1 for easier calculation
        S = [[0] * (W + 1) for _ in range(H + 1)]
        for r in range(H):
            for c in range(W):
                val = bad_grid[r][c]
                S[r+1][c+1] = S[r][c+1] + S[r+1][c] - S[r][c] + val
                
        def is_valid_rect(cz1, rz1, cz2, rz2):
            # Check sum of bad block in range [rz1..rz2, cz1..cz2]
            # rz2, cz2 are inclusive indices in bad_grid
            # In S, we access rz2+1, cz2+1
            total_bad = S[rz2+1][cz2+1] - S[rz1][cz2+1] - S[rz2+1][cz1] + S[rz1][cz1]
            return total_bad == 0

        # 5. Solver Loop
        max_area = 0
        n = len(original_coords)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = original_coords[i]
                x2, y2 = original_coords[j]
                
                # Check validity in compressed space
                cx1, cy1 = x_map[x1], y_map[y1]
                cx2, cy2 = x_map[x2], y_map[y2]
                
                c_min, c_max = min(cx1, cx2), max(cx1, cx2)
                r_min, r_max = min(cy1, cy2), max(cy1, cy2)
                
                if is_valid_rect(c_min, r_min, c_max, r_max):
                    # Calculate Area using ORIGINAL coordinates
                    width = abs(x1 - x2) + 1
                    height = abs(y1 - y2) + 1
                    area = width * height
                    if area > max_area:
                        max_area = area
                        
        return max_area
