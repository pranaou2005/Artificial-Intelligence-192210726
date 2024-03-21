% Define facts and rules

% Rule: If it's hot, then turn on the fan
action(turn_on_fan) :- 
    temperature(high).

% Rule: If it's cold, then turn on the heater
action(turn_on_heater) :- 
    temperature(low).

% Rule: If there's smoke, then there's a fire
fire :- 
    smoke.

% Facts
temperature(high). % It's hot
smoke. % There's smoke

% Initialize inferred actions
:- dynamic inferred/1.

% Forward chaining inference
infer_actions :-
    action(Action), % Find possible actions
    not(inferred(Action)), % Check if action not already inferred
    assertz(inferred(Action)), % Assert inferred action
    write('Infer: '), write(Action), nl, % Print inferred action
    fail. % Force backtracking to find more actions
infer_actions. % Recursively infer more actions

% Query to initiate forward chaining inference
start_forward_chaining :-
    infer_actions,
    retractall(inferred(_)). % Remove inferred facts after inference


