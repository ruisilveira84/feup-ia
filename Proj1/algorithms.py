from collections import deque
import heapq
from gamelogic import *
from levels import *
import time


# TreeNode modelo
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

        

def breadth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)   # create the root node in the search tree
    queue = deque([root])   # initialize the queue to store the nodes
    state_list = set()
    state_list.add(initial_state)
    i = 0
    while queue:
        node = queue.popleft()   # get first element in the queue
        if check_win(node.state.board,node.state.final_board):   # check goal state
            return node
        state_list.add(node.state)
        for state in operators_func(node.state):
            if(state not in state_list):   # go through next states
                # create tree node with the new state
                newNode = TreeNode(state)
            
                # link child node to its parent in the tree
                node.add_child(newNode)

                state_list.add(state)
                #i+=1
                #print(i)
            
                # enqueue the child node
                queue.append(newNode)

    return



def a_star_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer

    
    initial_state = problem
    # this is very similar to greedy, the difference is that it takes into account the cost of the path so far
    return greedy_search(problem, lambda state: heuristic(state) + (heuristic(state) - heuristic(initial_state)))

def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
    root = TreeNode(initial_state)
    visited = set()
    result = depth_limited_search_rec(root,goal_state_func,operators_func,visited,depth_limit,0)
    if(result != None):
        return result
    return None

def depth_limited_search_rec(node, goal_state_func, operators_func, state_list,depth_limit,current_depth):
    if(check_win(node.state.board , node.state.final_board)):  # create the root node in the search tree
        return node
    if current_depth == depth_limit:
        # print(current_depth)
        return None
      
    for state in operators_func(node.state):
        if(state not in state_list):
            # print(current_depth)
            # create tree node with the new state
            newNode = TreeNode(state)

            node.add_child(newNode)

            result = depth_limited_search_rec(newNode,goal_state_func,operators_func,state_list,depth_limit,current_depth+1)
            if(result != None):
                return result
    return None



def iterative_deepening_search(initial_state, goal_state_func, operators_func):
    depth_limit = 1
    while True:
        result = depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

def a_star_search_limited_time(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer

    
    initial_state = problem
    # this is very similar to greedy, the difference is that it takes into account the cost of the path so far
    return greedy_search_limited_time(problem, lambda state: heuristic(state) + (heuristic(state) - heuristic(initial_state)))

def greedy_search_limited_time(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    # Mudar o NPuzzle
    setattr(Cogito, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice
    current_state = problem
    heap_states = []
    start = time.time()

    while states:
        if check_win(current_state.board,current_state.final_board):
            return current_state.move_history
        end = time.time()
        if (end - start) >= 1:
            return current_state.move_history
        visited.add(current_state)
        children_states = get_moves(current_state)
        for c_state in children_states:
            heapq.heappush(heap_states,c_state)
            
        next_state = heapq.heappop(heap_states)

        while next_state in visited:
            if not heap_states:  # If no unvisited neighbors, break out of loop
                next_state = None
                break
            next_state = heapq.heappop(heap_states)

        
        current_state = next_state
            
        # TO COMPLETE
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        # ...
        # ...
        
    return None

def greedy_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    # Mudar o NPuzzle
    setattr(Cogito, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice
    current_state = problem
    heap_states = []

    while states:
        if check_win(current_state.board,current_state.final_board):
            return current_state.move_history
        visited.add(current_state)
        children_states = get_moves(current_state)
        for c_state in children_states:
            heapq.heappush(heap_states,c_state)
            
        next_state = heapq.heappop(heap_states)

        while next_state in visited:
            if not heap_states:  # If no unvisited neighbors, break out of loop
                next_state = None
                break
            next_state = heapq.heappop(heap_states)

        
        current_state = next_state
            
        # TO COMPLETE
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        # ...
        # ...
        
    return None

def _preferential_position(number, side):
    # calculates the preferred position of a piece given its number
    # number (int) - the number of the piece
    # side (int) - the size of the side of the board (only for square boards)
    if number == 0:
        # if it is the last piece, it is 0
        row = col = side - 1
    else:
        # otherwise it is sequential, starting at 1
        row = number // side
        col = number % side - 1
    return (row, col)

def h1(state):
    # heuristic function 1
    # returns the number of incorrect SPECIAL placed pieces in the matrix
    board = state.board
    desired_board = state.final_board
    side = len(board) # the size of the side of the board (only for square boards)

    total = 0
    
    # checks if the board is complete
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == Piece.SPECIAL and desired_board[row][col] != board[row][col]:
                total += 1
    return total
def find_nearest_piece(board,row,col,desired_board):
    # Esta funcao retorna a localizacao da peça mais proxima no tabuleiro final da peça desejada, que nao esta preenchida
    searching_row=1
    searching_col=1
    not_found = True
    possible_cases = []
    while not_found:
        for row_search in range(-searching_row,searching_row+1):
            if (len(board)-1) >= row_search+row and row_search+row>=0:
                for col_search in range(-searching_col,searching_col+1):
                    if (len(board)-1) >= col_search+col and col_search+col>=0 and (col_search,row_search) != (0,0) and board[row_search+row][col_search+col] != Piece.SPECIAL and desired_board[row_search+row][col_search+col]==Piece.SPECIAL:
                        possible_cases.append((row_search+row,col_search+col))
        if(len(possible_cases))>0:
            sort = sorted(possible_cases,key=lambda x: abs(row - x[0]) + abs(col - x[1]))
            return sort[0]
        searching_row+=1
        searching_col+=1
        if searching_row==len(board):
            return None
def h2(state):
    # heuristic function 2
    # returns the sum of manhattan distances from incorrect placed pieces to their correct places
    board = state.board
    desired_board = state.final_board
    side = len(board) # the size of the side of the board (only for square boards)

    total = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == Piece.SPECIAL and desired_board[row][col] != board[row][col]:
                (desired_row,desired_col) = find_nearest_piece(board,row,col,desired_board)
                total += abs(col-desired_col) + abs(row-desired_row)
    return total

def print_solution(node):
    if node == None:
        print("None solution was found!")
        return
    while node != None:
        print(node.state)
        node = node.parent
    
    return

def print_sequence(sequence):
    print("Steps:", len(sequence) - 1)
    # prints the sequence of states
    for state in sequence:
        for row in state:
            print(row)
        print()
"""
goal = iterative_deepening_search(Cogito(levels["Beginner"][0]["initial_state"],levels["Beginner"][0]["objective_state"]), check_win,get_moves)
print_sequence(goal)
"""
"""[
                                [1, 0, 0, 1, 0],
                                [1, 1, 0, 1, 1],
                                [0, 1, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                            ]"""
"""
start = time.time()
print_sequence(a_star_search_limited_time(Cogito(levels["Expert"][0]["initial_state"],levels["Expert"][0]["objective_state"]),h2))
end = time.time()
print(end - start)

# print(check_win(Cogito([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 0, 0, 0, 0]],[[1, 0, 0, 1, 0],[1, 1, 0, 1, 1],[0, 1, 0, 0, 1],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0]])))
# print(check_win(Cogito([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 1, 1, 1, 0],[0, 0, 0, 0, 0]])))
"""