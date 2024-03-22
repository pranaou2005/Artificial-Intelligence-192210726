bird(canary).
bird(sparrow).
bird(penguin).

can_fly(canary).
can_fly(sparrow).

flies(X) :-
    bird(X),
    can_fly(X),
    write(X), write(' can fly.'), nl.
flies(X) :-
    bird(X),
    \+ can_fly(X),
    write(X), write(' cannot fly.'), nl.