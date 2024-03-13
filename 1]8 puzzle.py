import heapq

class PuzzleState:
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Final state of the puzzle
    
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __hash__(self):
        return hash(str(self.state))

    def get_blank_pos(self):
        return self.state.index(0)

    def get_children(self):
        children = []
        blank_index = self.get_blank_pos()
        if blank_index // 3 > 0:
            new_state = self.state[:]
            new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
            children.append(PuzzleState(new_state, self, 'Up'))
        if blank_index // 3 < 2:
            new_state = self.state[:]
            new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
            children.append(PuzzleState(new_state, self, 'Down'))
        if blank_index % 3 > 0:
            new_state = self.state[:]
            new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
            children.append(PuzzleState(new_state, self, 'Left'))
        if blank_index % 3 < 2:
            new_state = self.state[:]
            new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
            children.append(PuzzleState(new_state, self, 'Right'))
        return children

    def is_goal(self):
        return self.state == self.goal_state

    def heuristic(self):
        return sum([1 if self.state[i] != self.goal_state[i] else 0 for i in range(8)])

def a_star(start_state):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, start_state)

    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.is_goal():
            return current_state
        closed_set.add(current_state)
        for child in current_state.get_children():
            if child in closed_set:
                continue
            heapq.heappush(open_set, child)
    return None

def print_solution(solution_state):
    if solution_state is None:
        print("No solution found.")
    else:
        path = []
        current_state = solution_state
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        path.reverse()
        for state in path:
            print(state.state[:3])
            print(state.state[3:6])
            print(state.state[6:9])
            print()

if __name__ == "__main__":
    initial_state = [1, 2, 3, 0, 4, 5, 6, 7, 8]  # Initial state of the puzzle
    start_state = PuzzleState(initial_state)
    solution = a_star(start_state)
    print_solution(solution)
