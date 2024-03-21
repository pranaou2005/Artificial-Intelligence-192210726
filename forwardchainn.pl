% Define the rules
parent(john, mary).
parent(mary, ann).
parent(mary, bob).
parent(bob, lisa).
parent(bob, johnny).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

forward_ancestor(X, Y) :-
    parent(X, Y).
forward_ancestor(X, Y) :-
    parent(X, Z),
    forward_ancestor(Z, Y).
