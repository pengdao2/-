import time
import turtle as t

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

def draw_rect(color: tuple,size,pensize=2):
    t.color(*color)
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(size)
    t.end_fill()

def goto_fill(go_to: list,info_list):
    if info_list:
        t.penup()
        t.goto(*go_to)
        t.pendown()
        if info_list[0] == 1:
            draw_rect(('red','yellow'),40)
        else:
            draw_rect(('red', 'white'), 40)
        go_to[0] = go_to[0] + 40
        goto_fill(go_to,info_list[1:])

def search_path(go_to,color):
    t.penup()
    t.goto(*go_to)
    t.pendown()
    draw_rect(color, 40)

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
            # for i in stack:
            #     search_path([-200 + i[1] * 40, 200 - i[0] * 40], ('red', 'yellow'))
            t.write('找到了')
            return '找到了'
        for dir in dirs:
            nextNode = dir(*currNode)
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                search_path([-200 + nextNode[1] * 40, 200 - nextNode[0] * 40], ('red', 'yellow'))
                break
        else:
            stack.pop()
            search_path([-240 + nextNode[1] * 40, 200 - nextNode[0] * 40], ('red', 'white'))
    else:
        t.write('没找到')

if __name__ == '__main__':
    import copy
    maze_copy = copy.deepcopy(maze)
    t.screensize(800,800)
    t.speed(10000)
    for i in range(10):
        goto_fill([-200,200-i*40],maze_copy[i])
    t.speed(30)
    get_maze_path(1,1,8,8)
    input()