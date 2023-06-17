def solve_maze(maze):
    # Helper function to check if a cell is valid and can be visited
    def is_valid_move(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        elif maze[row][col] == '#':
            return False
        elif visited[row][col]:
            return False
        return True

    # Helper function to print the maze
    def print_maze():
        for row in maze:
            print(''.join(row))
        print()

    # Helper function to recursively explore the maze
    def explore(row, col):
        # Mark current cell as visited
        visited[row][col] = True

        # Check if we reached the exit
        if (row, col) == exit_pos:
            print_maze()  # Print the final solution
            return True

        # Try all possible moves: up, right, down, left
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if is_valid_move(new_row, new_col):
                # Move to the next cell
                maze[new_row][new_col] = '.'
                print_maze()  # Print the current state of the maze
                if explore(new_row, new_col):
                    return True  # Exit found, terminate recursion

                # Dead end, backtrack
                maze[new_row][new_col] = ' '
                print_maze()  # Print the backtracking state

        return False

    # Get the maze dimensions
    rows = len(maze)
    cols = len(maze[0])

    # Find the start and exit positions
    start_pos = None
    exit_pos = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start_pos = (i, j)
            elif maze[i][j] == 'E':
                exit_pos = (i, j)

    if start_pos is None or exit_pos is None:
        print("Invalid maze: Start or exit position not found.")
        return

    # Initialize visited array
    visited = [[False] * cols for _ in range(rows)]

    # Define the possible moves: up, right, down, left
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Start exploring from the start position
    maze[start_pos[0]][start_pos[1]] = '.'
    print_maze()  # Print the initial state of the maze
    if not explore(start_pos[0], start_pos[1]):
        print("No path found.")

# Example maze (S: Start, E: Exit, #: Walls)
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '#', '#', '#', '#', '#', '#
