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
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
]

def get_maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1,y1))
    while stack:
        currNode = stack[-1]
        if currNode == (x2,y2):
            print(*stack)
            return '找到了'
        for dir in dirs:
            nextNode = dir(*currNode)
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            stack.pop()
    else:
        return '找不到'
print(get_maze_path(1, 1, 8, 8))
