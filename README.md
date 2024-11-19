# war_cardgame

Create a playable War Card Game:

Functional requirements:
1. Game must be playable against a CPU
2. Player can choose to play with either a full deck or only "high cards" (9s and up)
  2.1. Choise input must be a command-line argument
  2.2. Invalid user inputs should quit the program with an error message
  4. Implement game loop:
     3.1 Players get dealt equal amount of cards from a randomly shuffled deck.
     3.2 After user input a single round of the game commences.
     3.3 Game waits for user input after each round to continue.
     3.4 Player's card count must be visible to the user at all times
     3.5 When game ends, a congratulatory message is shown and user is prompted to play again.

Non-functional requirements:
  1. Project must be designed to allow for future expansion

Technical requirements:
  1. Project must be built with python, using OOP principles
  2. Project must use Python's module system, organizing code into separate files that group
     related functions, classes and constants for better modularity and readability.
    
