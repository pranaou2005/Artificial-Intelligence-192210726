% Define the rules
parent(john, mary).
parent(mary, ann).
parent(mary, bob).
parent(bob, lisa).
parent(bob, johnny).

% Define the recursive rule for ancestor
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Query to find all ancestors of a person
% Example Query: ?- ancestor(john, X).
% This will find all ancestors of john