# TicTacToe
TicTacToe related programs and AIs. Dependent on one another.

## RoteAI
A program built with a knowledge of how to win TTT. It cannot lose under any circumstances. It goes first, and follows 
a very complex tree of evaluations.

However, I wrote it a long time ago. It is not at all modular, and can only run on its own. It's now essentially legacy 
code that may be used in a later version of the AI that is modular. It may be resurrected, but only to test the system.
In terms of code, it's just not a very good system.

## Interface
This is really the heart and soul of the system. It contains the object Game() which runs the game. I think the code is
pretty well-documented, so I won't describe it here, but it does a good job of handling the two ends of the program, de
ling with the board, etc.

## Human
This is the first end I made for Interface. It just asks for user input, and that's it. It takes on instantiation eithe
r player1 or player2, so if you play pvp, it can make clear what side you're giving input for.

## PvP
Much like RoteAI, this is legacy code from when I originally wrote this program. It will only serve as a place to get s
ome important methods, like the win determination code. It really doesn't need to be in the repo, as it's not changing,
but it makes life easier when rolling code over.
