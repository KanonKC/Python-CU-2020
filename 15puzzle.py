# Prog-06: 8-Puzzle
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

def is_goal(node): 
    return node[:-1] == \
           list(range(1,len(node)-1))+[0]

def insert_all(node, fringe):
    n = len(node)
    children = gen_successors(node)
    for i in range(0,len(children),n):
        fringe.append(children[i:i+n])

def bfs(board):
    start_node = board + ['']
    fringe = [start_node]
    while True:
        if len(fringe) == 0:
            break
        front = fringe[0]
        fringe = fringe[1:]
        if is_goal(front):
            return front[-1]
        insert_all(front,fringe) 
    return ''

def print_successors(s):
    N = 1
    for e in s:
        if type(e) is str: break
        N += 1
    for i in range(0,len(s),N):
        print(s[i:i+N])
#---------------------------------------
def gen_successors(node):
    successors = []
    move = [
        'DR','DLR','DL',
        'UDR','UDLR','UDL',
        'UR','ULR','UL',
    ]
    a = node.index(0) # 8
    zero = move[a]
    node2 = [i for i in node]
    
    for i in move:
        node2.remove(0)
        if i == 'U':
            node2.insert(a-3,0)
            node2.insert(a+1,node2[a-2])
            node2.pop(a-4)
        elif i == 'D':

        elif i == 'L':

        elif i == 'R':

# [4,1,3,
#  2,5,0
#  6,7,8, ]

            
    return successors 
#------------------------------------------
def print_moves(board, moves):
    # bonus function: optional


    pass
#------------------------------------------
board = [4,1,3,
         2,5,6,
         7,8,0]
s = gen_successors(board + ['UDR']) # We're doing here
print_successors(s)
moves = bfs(board)
print(moves)
print_moves(board, moves) # optional bonus