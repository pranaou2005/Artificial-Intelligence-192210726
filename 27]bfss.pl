% Define graph edges and their costs
edge(a, b, 3).
edge(a, c, 5).
edge(b, d, 8).
edge(b, e, 12).
edge(c, f, 10).
edge(c, g, 6).
edge(d, h, 9).
edge(e, i, 7).
edge(f, j, 4).
edge(g, k, 11).

% Heuristic function to estimate the distance from a node to the goal node
heuristic(a, 15).
heuristic(b, 10).
heuristic(c, 12).
heuristic(d, 6).
heuristic(e, 10).
heuristic(f, 8).
heuristic(g, 9).
heuristic(h, 4).
heuristic(i, 7).
heuristic(j, 5).
heuristic(k, 0).  % Heuristic value for the goal node is 0

% Best-First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search_aux([node(Start, 0)], Goal, [], Path).

% Base case: Goal node is reached
best_first_search_aux([node(Goal, _)|_], Goal, AccPath, Path) :-
    reverse([Goal|AccPath], Path).

% Recursive case: Expand the current node and continue the search
best_first_search_aux([node(Current, _)|Rest], Goal, AccPath, Path) :-
    findall(node(Next, H), (edge(Current, Next, _), heuristic(Next, H)), Children),
    merge(Children, Rest, NewOpen),
    best_first_search_aux(NewOpen, Goal, [Current | AccPath], Path).

% Merge two lists of nodes by sorting based on their heuristic values
merge([], Open, Open).
merge(Open, [], Open).
merge([X|Open1], [Y|Open2], Merged) :-
    compare_nodes(X, Y, Result),
    merge(Result, X, Open1, Y, Open2, Merged).

% X has a smaller heuristic value, so keep X first
merge(<, X, Open1, Y, Open2, [X|Merged]) :-
    merge(Open1, [Y|Open2], Merged).

% Y has a smaller heuristic value, so keep Y first
merge(>, X, Open1, Y, Open2, [Y|Merged]) :-
    merge([X|Open1], Open2, Merged).

% Compare nodes based on their heuristic values
compare_nodes(node(_, H1), node(_, H2), Result) :-
    compare(Result, H1, H2).

