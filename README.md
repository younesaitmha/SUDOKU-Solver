# SUDOKU-Solver

Sudoku solver with python, I'm gonna explain how we can solve sudoku problem with the algorithm known as backtracking.

## **Algorithm**

**What is backtracking algorithm?**

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, that incrementally builds candidates to the solutions, and abandons each partial candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Starting with an incomplete board:

* Find the first empty space if it exist
* Attempt to place the digits 1-9 in that space
* Check if that digit is valid in the current spot based on the current board
* attempt the board with backtrack
  + If the digit is valid, recursively attempt to fill the board using steps 1-3.
  + If it is not valid, reset the square you just filled and go back to the previous step.
* Once the board is full by the definition of this algorithm we have found a solution.

## Requirements

To install [pygame](https://www.pygame.org/wiki/GettingStarted)\
or
> python3 -m pip install pygame==2.0.0.dev6

## Instructions

* Choose the level
* Click a box and hit the number on your keybaord to pencil in a number.
* To confirm that value press the ENTER key on that box.
* To delete a pencil in, you can click DEL.
* To solve the board press SPACE.

## Reference

* [freecodecamp](https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/)
* [Pygame Tutorial](https://www.youtube.com/watch?v=FfWpgLFMI7w)
