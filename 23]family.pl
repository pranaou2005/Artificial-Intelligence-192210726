male(john).
male(mike).
male(bob).
male(james).
male(alex).

female(anna).
female(susan).
female(emily).
female(sarah).

parent(john, mike).
parent(john, anna).
parent(anna, susan).
parent(mike, bob).
parent(anna, emily).
parent(susan, james).
parent(emily, sarah).
parent(bob, alex).


father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
