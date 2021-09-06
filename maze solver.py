#Shadowfray
#Maze solver - inspired by Timur Bakibayev

start = 1, 1
end = 2,5

def makeMaze(height, width):
    #currently just holds a test maze
    maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

    return maze

def findWalls(maze,mazecopy,k):
    #checks in the cardinal directions if there is an empty space
    for i in range(len(mazecopy)):
        for j in range(len(mazecopy[i])):
          if mazecopy[i][j] == k:
            if i>0 and mazecopy[i-1][j] == 0 and maze[i-1][j] == 0:
              mazecopy[i-1][j] = k + 1
            if j>0 and mazecopy[i][j-1] == 0 and maze[i][j-1] == 0:
              mazecopy[i][j-1] = k + 1
            if i<len(mazecopy)-1 and mazecopy[i+1][j] == 0 and maze[i+1][j] == 0:
              mazecopy[i+1][j] = k + 1
            if j<len(mazecopy[i])-1 and mazecopy[i][j+1] == 0 and maze[i][j+1] == 0:
               mazecopy[i][j+1] = k + 1

def findpath(maze, mazecopy,point):
    pos = [end[0],end[1]]
    moveshome = []

    #checks each cardinal direction for the lesser value and follow it backwards
    while point != 1:

        if mazecopy[pos[0]][pos[1] + 1] == point - 1:
            pos[1] += 1
            point -= 1
            moveshome.append([pos[0],pos[1]])

        if mazecopy[pos[0]][pos[1] - 1] == point - 1:
            pos[1] -= 1
            point -= 1
            moveshome.append([pos[0],pos[1]])

        if mazecopy[pos[0] - 1][pos[1]] == point - 1:
            pos[0] -= 1
            point -= 1
            moveshome.append([pos[0],pos[1]])

        if mazecopy[pos[0] + 1][pos[1]] == point - 1:
            pos[0] += 1
            point -= 1
            moveshome.append([pos[0],pos[1]])
               
    return moveshome


def main_pathfinder(height, width):
    maze = makeMaze(height, width)
    height, width = len(maze), len(maze[0])
    
    #make a blank copy of the maze
    mazecopy = []
    for mazecount_i in range(height):
        mazecopy.append([])
        for mazecount_j in range(width):
            mazecopy[mazecount_i].append(0)
    mazecopy[start[0]][start[1]] = 1

    #checks if the value at the end is still 0 and places steps
    n = 0
    while mazecopy[end[0]][end[1]] == 0:
        n += 1
        findWalls(maze,mazecopy,n)
    endpoint = mazecopy[end[0]][end[1]]

    #finds the path to and from the given point
    moveshome = findpath(maze, mazecopy,endpoint)
    moveshome.reverse()
    #prints the moves needed for debugging
    #print(moveshome)

    #prints the steps the program took for debugging
    #for i in range(len(maze)):
        #print(mazecopy[i])

    for path_i in moveshome:
        maze[path_i[0]][path_i[1]] = 6
    for m in range(len(maze)):
        print(maze[m])

main_pathfinder(10,10)
        
