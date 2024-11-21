male(matija).
male(martin).
male(miha).
male(ales).
male(slavko).
male(marko).
male(maks).
male(filip).
male(samo).
female(melita).
female(marta).
female(nina).
female(damjana).
female(anika).
parent(ales,matija).
parent(ales,martin).
parent(ales,miha).
parent(melita,matija).
parent(melita,martin).
parent(melita,miha).
parent(slavko,melita).
parent(marta,melita).
parent(slavko,damjana).
parent(marta,damjana).
parent(slavko,marko).
parent(marta,marko).
parent(marko,maks).
parent(nina,maks).
parent(marko,anika).
parent(nina,anika).
parent(damjana,filip).
parent(damjana,samo).

grandmother(A,B) :-
    female(A),
    parent(A,O),
    parent(O,B).

grandfather(A,B) :-
    male(A),
    parent(A,O),
    parent(O,B).

sibling(A,B) :-
    parent(O,A),
    parent(O,B),
    A\=B.

cousin(A,B) :-
    grandfather(O,A),
    grandfather(O,B),
    A\=B;
    grandmother(O,A),
    grandmother(O,B),
    A\=B.

aunt(A,B) :-
    female(A),
    parent(O,B),
    sibling(O,A).  

uncle(A,B) :-
    male(A),
    parent(O,B),
    sibling(O,A).

nephew(A,B) :-
    aunt(B,A);
    uncle(B,A).