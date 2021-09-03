def print_uppertri(N,w):
    maze = [[] for i in range(N)]
    num = 1
    for i in range(N):
        for j in range(N-i):
            maze[j].append(str(num))
            num += 1
    # =================================
    formatMaze = []
    for i in range(len(maze)):
        subFormat = ""
        for j in range(len(maze[i])):
            dot = w - len(maze[i][j])
            subFormat += ("."*dot)+maze[i][j]
        formatMaze.append(subFormat)
    # =================================
    for i in range(len(formatMaze)):
        while len(formatMaze[i]) < len(formatMaze[0]):
            formatMaze[i] = "." + formatMaze[i]
        print(formatMaze[i])


print_uppertri(7,4)