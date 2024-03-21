% Define the initial state of the monkey and the bananas in the room
initial_state(location(middle, on_floor), location(box, on_floor), location(bananas, ceiling), has_not).

% Define actions that the monkey can take
move(location(X, on_floor), location(X, on_box)) :-
    reachable(X).
move(location(X, on_box), location(X, on_floor)) :-
    reachable(X).
move(location(X, on_floor), location(Y, on_floor)) :-
    reachable(X),
    reachable(Y),
    X \= Y.

% Define the goal state where the monkey has the bananas
goal_state(_, _, location(bananas, on_floor), has).

% Define a predicate to check if a location is reachable
reachable(middle).
reachable(left).
reachable(right).

% Define a predicate to solve the problem using depth-first search
solve_dfs(State, _, Actions, Actions) :-
    goal_state(State, _, _, _).
solve_dfs(State, Visited, Actions, AllActions) :-
    \+ member(State, Visited),
    transition(State, NextState, Action),
    solve_dfs(NextState, [State | Visited], [Action | Actions], AllActions).

% Define a predicate to solve the problem using depth-first search and return the list of actions
solve(State, Actions) :-
    solve_dfs(State, [], [], Actions).

% Define a predicate to perform a transition from one state to another
transition(State1, State2, Action) :-
    valid_transition(State1, State2, Action).

% Define a predicate to check if a state transition is valid
valid_transition(State1, State2, Action) :-
    State1 =.. [location | Args1],
    State2 =.. [location | Args2],
    Action =.. [move | [Location1, Location2]],
    member(Location1, Args1),
    member(Location2, Args2),
    Location1 \= Location2.
