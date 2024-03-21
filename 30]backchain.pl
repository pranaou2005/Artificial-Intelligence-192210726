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

% Backward chaining inference
infer_action(Action) :-
    action(Action), % Check if Action can be inferred
    check_conditions(Action). % Check if conditions for Action are satisfied

check_conditions(turn_on_fan) :-
    temperature(high). % If it's hot
check_conditions(turn_on_heater) :-
    temperature(low). % If it's cold
check_conditions(fire) :-
    smoke. % If there's smoke

% Query to initiate backward chaining inference
start_backward_chaining(Action) :-
    infer_action(Action),
    write('Action to be taken: '), write(Action), nl.


