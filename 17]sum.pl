sum_numbers(0,0).
sum_numbers(N,Sum):-
    N > 0,
    Prev is N-1,
    sum_numbers(Prev,PrevSum),
    Sum is PrevSum + N.

