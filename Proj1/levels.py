# levels.py

class Piece:
    NORMAL = 0
    SPECIAL = 1
    

class Level:
    def __init__(self, initial_state, objective_state):
        self.initial_state = initial_state
        self.objective_state = objective_state


beginner_1 = {
    "initial_state": [
        [Piece.NORMAL,Piece.SPECIAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.SPECIAL,Piece.SPECIAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.SPECIAL,Piece.SPECIAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.SPECIAL,Piece.SPECIAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.SPECIAL,Piece.SPECIAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.SPECIAL,Piece.SPECIAL,Piece.SPECIAL,Piece.NORMAL],
        [Piece.NORMAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL,Piece.NORMAL],
        
    ],
}


beginner_2 = {
    "initial_state": [
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}

beginner_3 = {
    "initial_state": [
        [Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}


amateur_1 = {
    "initial_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}


amateur_2 = {
    "initial_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}

amateur_3 = {
    "initial_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}


expert_1 = {
    "initial_state": [
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}


expert_2 = {
    "initial_state": [
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}

expert_3 = {
    "initial_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
    "objective_state": [
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.SPECIAL, Piece.SPECIAL, Piece.SPECIAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
        [Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL, Piece.NORMAL],
    ],
}

# Dicionário de todos os níveis para fácil acesso
levels = {
    "Beginner": [beginner_1, beginner_2, beginner_3],
    "Amateur": [amateur_1, amateur_2, amateur_3],
    "Expert": [expert_1, expert_2, expert_3],
}