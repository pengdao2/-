from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y:(x-1,y),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y+1),
    lambda x,y:(x,y-1),
]

def print_f(path):
    currNode = path[-1]
    info = []
    while currNode[2] != -1:
        info.append(currNode[0:2])
        currNode = path[currNode[2]]
    info.append(currNode[0:2])
    info.reverse()
    print(*info)

def queue_maze_path(x1,y1,x2,y2):
    queue = deque()
    path = []
    queue.append((x1,y1,-1))
    while queue:
        currNode = queue.pop()
        path.append(currNode)
        if currNode[0] == x2 and currNode[1] == y2:
            print_f(path)
            return print('找到了')
        for dir in dirs:
            nextNode = dir(currNode[0],currNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        return print('找不到')

queue_maze_path(1,1,8,8)