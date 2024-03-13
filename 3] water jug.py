class WaterJugProblem:
    def __init__(self, capacity_x, capacity_y, target):
        self.capacity_x = capacity_x
        self.capacity_y = capacity_y
        self.target = target
        self.visited_states = set()
        self.solution_path = []

    def solve(self):
        initial_state = (0, 0)  # Initial state: both jugs are empty
        if self._dfs(initial_state):
            self.solution_path.reverse()
            for state in self.solution_path:
                print(state)
        else:
            print("No solution found.")

    def _dfs(self, current_state):
        if current_state[0] == self.target or current_state[1] == self.target:
            self.solution_path.append(current_state)
            return True

        self.visited_states.add(current_state)

        next_states = [
            (self.capacity_x, current_state[1]),  # Fill jug x
            (current_state[0], self.capacity_y),  # Fill jug y
            (0, current_state[1]),  # Empty jug x
            (current_state[0], 0),  # Empty jug y
            (min(self.capacity_x, current_state[0] + current_state[1]), max(0, current_state[0] + current_state[1] - self.capacity_y)),  # Pour from x to y
            (max(0, current_state[0] + current_state[1] - self.capacity_x), min(self.capacity_y, current_state[0] + current_state[1]))   # Pour from y to x
        ]

        for state in next_states:
            if state not in self.visited_states:
                self.solution_path.append(current_state)
                if self._dfs(state):
                    return True
                self.solution_path.pop()

        return False

if __name__ == "__main__":
    capacity_x = 4  # Capacity of jug x
    capacity_y = 3  # Capacity of jug y
    target = 2      # Target amount of water

    problem = WaterJugProblem(capacity_x, capacity_y, target)
    problem.solve()
