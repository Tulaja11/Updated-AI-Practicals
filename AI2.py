import heapq

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []  
    heapq.heappush(open_list, (0 + manhattan_distance(start, goal), 0, start))  # (f, g, (x, y))
    
    g_cost = {}  
    g_cost[start] = 0
    
    came_from = {}  
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()  
            return path
        
        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_g = g + 1  
                
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_list, (f, new_g, neighbor))
                    came_from[neighbor] = current
    
    return None  

def get_user_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    grid = []
    print("Enter the grid values (0 for open path, 1 for obstacle):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grid.append(row)
    
    start = tuple(map(int, input("Enter start position (row col): ").split()))
    goal = tuple(map(int, input("Enter goal position (row col): ").split()))
    
    return grid, start, goal

def main():
    grid, start, goal = get_user_input()

    path = a_star(grid, start, goal)
       
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
