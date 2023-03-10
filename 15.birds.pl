bird(eagle).
bird(penguin).
bird(ostrich).
bird(dodo).
bird(sparrow).
bird(pigeon).

flightless_bird(penguin).
flightless_bird(ostrich).
flightless_bird(dodo).

bird_of_pray(eagle).

extinct(dodo).
extinct(wooly_mammoth).

can_fly(Bird) :-
    bird(Bird),
    \+ flightless_bird(Bird).

extinct_bird(Bird) :-
    bird(Bird),
    extinct(Bird).
