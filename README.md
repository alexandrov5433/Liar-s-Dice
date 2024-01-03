# Liar-s-Dice

#### Video Demo: https://youtu.be/6UuMGKgPqck

#### Description:
Liar´s Dice is the final project of Aleksandar Darakev for the CS50p course. The implemented program is a game called Liar´s Dice. In this 
version, two players - the user and the computer - play against each other. The rules of this Liar´s Dice are as follows: The game is 
played over multiple rounds. The first player for the first round is determined by rock, paper, scissors.
To begin each round, all players roll their dice simultaneously. Each player looks at their own dice after they roll, keeping them hidden 
from the other players.
The first player then states a bid consisting of a face and a quantity - e.g. 2x5, two dice of fives. The quantity represents the player's 
guess as to how many of each face have been rolled by all the players, including themselves.
Each subsequent player can either then make a higher bid of the same face - e.g 3x5 -, or they can call the previous player a liar. A 
player may bid a higher quantity of the same face - e.g 3x5 -, or the same quantity of a higher face - e.g. 2x6. 
If liar is called, all players reveal their dice. If the bid is matched or exceeded, the bidder wins. Otherwise the challenger wins. The 
losing player of the round loses 1 die. The loser of the previous round begins the next round.

#### Pre-Programing decisions:
Before starting with the project different versions of Liar´s Dice were reviewed. They differ, more or less, in additional rules like 
“Wild Ones – a one can represent any number”, dice rolling sequence, calling etc. None of them were implemented in this basic version of 
the game, as the complexity of it – from a coding standpoint – is already fairly high for an introduction course.
The other important decision was on how to establish a connection between the different functions. The fact that they were already to be 
inside of `main()` was not sufficient, as the same values would be used multiple times across the code on different levels; would need to 
be changed in the middle of the process from different functions and again retrieved. The first, most simple, thought-of solution was to 
create multiple variables in the scope of `main()`. Nevertheless, this did not seem as if it would suffice, first because of the needs 
mentioned prior and second, and most important, because we would need to work with the given values and every time receive a consistent 
output –which meant more functions. As a result, a class was chosen to store and process values and to connect functions – `Connector()`.

#### Code functionality of project.py:
The program consists of a class, a main function and three additional functions. The three additional functions are: `start_RPS()`, 
`dice_roller()` and `score_updater()`.    
The `start_RPS()` is the function through which the starting player in the beginning of the game is determined. This is done as the user 
plays “Rock, paper, scissors” with the computer. The computer asks the user for a rock, paper or scissors. The input is taken and compared 
with the independently generated counterpart of the computer in multiple `if`- `elif` statements. If the words match, the user is prompted 
again. This is possible thanks to the while-loop, in which the checking in implemented. The winner of the mini-game is decided and 
returned from `start_RPS()` as a string – “user” or “robot”.    
The `dice_roller()`, as its name implies, has the sole purpose to “roll the dice” for each player. The function receives the number of 
dice for each player for the present roll in the form of a dictionary from the `Connector()` as an input. Example with 5 dice per player: 
`{"user":"12345","robot":"12345"}`. Using `random.randint(1, 6)` in a `for`-loop the dice of each player are generated and stored 
separately in lists. The dice of the user and the number of dice of the computer are printed in the terminal. The function ends by 
returning the lists of rolled dice, each as values of different keys in a dictionary.          
The function `score_updater()` activates at the end of each round. It receives as input firstly the winner of the round and secondly the 
dice count of each player in the form of a dictionary, provided by the `Connector()`. This dictionary has the players as keys – strings – 
and their respective dice count as values, the type of which is an integer. Based on who is the inputted round winner the 
`score_updater()` reduces the inputted dice count of the loser by one and returns a list: On index 0 is the loser as a string and on index 
1 is his new reduced dice count as an integer.     
The `Connector()` class is instantiated in the start of `main()` using the `connector` variable. Its purpose is to store different values 
in its class attributes – like strings, integers or dictionaries –, which are used and changed throughout the process by the previously 
mentioned functions. Some examples of variables stored in the `__init__ ` method are:     
`first_to_call`, with a default value of `"default"`, stores a string indicating the player who has to start the round. At the end of the 
round it is updated by the `update_first_to_call()` class method.      
The next two attributes `dice_quant_user` and `dice_quant_robot` store the number of dice for each player as integers. Their default 
values are the integer 5.      
On the forth position is `last_call` with a default string `“0x0”`. It saves the last call made of the last player. Its value is used by 
the `call_validator()` and `call()` class methods and is updated by the `update_last_call()`.    
The `last_pl_to_call ` saves the last player who has made a call as a string. Its default value is `“default”`.    
Lastly, `dice_dict` stores a dictionary with the rolled dice of each player provided by the function `dice_roller()`. Example: 
`{"user_rolled":[1, 2, 3, 4, 5],  "robot_rolled":[1, 2, 3, 4, 5]}`. The default value here is an empty dictionary `{}`.     
Some examples of class methods are:      
The `checker()` method uses `self.last_call` and `self.dice_dict` attributes to determine if the player who has called last and was called 
a liar is a winner or a loser. `last_call` stores the last call made. In `dice_dict` are the dice rolled by each player. It checks if the 
amount of dice with a certain face value from the `last_call` are actually present in the dice pool. Using  `last_pl_to_call` the method 
knows who has made the last call and returns the winner of the round as a string: `"robot"` or `"user"`.      
The `call()` method comes in effect when it is the turn of the computer. It returns either the string `“liar”` or a call, e.g. `“2x3”`, 
again of type string.      
The `main()` function of the program combines the different functions and is the core of the code. When project.py is run the program asks 
the user if he or she wants to read the rules of the game and instantiates the `Connector()` class. The actual gameplay follows in a 
series of nested `while`-loops, `if` functions and `try`-`except` error catching.  

#### Code functionality of test_project.py:
In test_project.py were tested multiple functions from the main file. Some of the functions could be tested strait forward with the assert 
function and set inputs and outputs.
The class methods were tested by first instantiating the class in a variable and then proceeding to the use of the assert function.
For the testing of the function `start_RPS()`, done in `test_start_RPS()`, the mock module was inported. By using the patch method of it 
the return value of the input function in `start_RPS()` was set, in order to avoid the – normally needed – user input. The same was done 
with the return value of the `random.randint()` function. Both “patches” were saved to variables and using a sequence of `start()`, 
`stop()` and assert functions the test could be successfully conducted.   






