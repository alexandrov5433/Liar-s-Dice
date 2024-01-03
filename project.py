import random
import collections
import re

class Connector():
    def __init__(self, first_to_call="default", dice_quant_user=5, dice_quant_robot=5, last_call="0x0", last_pl_to_call="default", dice_dict={}):
        self.first_to_call = first_to_call         
        self.dice_quant_user = dice_quant_user
        self.dice_quant_robot = dice_quant_robot
        self.last_call = last_call
        self.last_pl_to_call = last_pl_to_call 
        self.dice_dict = dice_dict          

    def dice_count(self):
        return {"user":self.dice_quant_user, "robot":self.dice_quant_robot}

    def call_validator(self, n):
        valid = True     
        if (re.fullmatch("[1-6]x[1-6]", n)) == None:
            valid = False
        elif int(n.split("x")[0]) <= int(self.last_call.split("x")[0]) and int(n.split("x")[1]) <= int(self.last_call.split("x")[1]):
            valid = False
        elif int(n.split("x")[0]) < int(self.last_call.split("x")[0]) and int(n.split("x")[1]) >= int(self.last_call.split("x")[1]):
            valid = False
        elif int(n.split("x")[0]) >= int(self.last_call.split("x")[0]) and int(n.split("x")[1]) < int(self.last_call.split("x")[1]):
            valid = False
        return valid

    def update_first_to_call(self, the_round_winner):
        if the_round_winner == "user":
            self.first_to_call = "robot"
        if the_round_winner == "robot":
            self.first_to_call = "user"

    def update_dice_dict(self, n):
        self.dice_dict = n

    def update_last_call(self, n):
        self.last_call = n

    def give_last_pl_to_call(self):
        return self.last_pl_to_call

    def update_last_pl_to_call(self, player):
        self.last_pl_to_call = player

    def dice_quant(self):
        dice_quant = True
        if self.dice_quant_user == 0:
            dice_quant = False
        if self.dice_quant_robot == 0:
            dice_quant = False
        return dice_quant

    def reduce_user_dice(self, new):
        self.dice_quant_user = new

    def reduce_robot_dice(self, new):
        self.dice_quant_robot = new

    def checker(self):                 
        round_winner = ""
        the_dice_list = self.dice_dict.get("user_rolled") + self.dice_dict.get("robot_rolled")
        d = int(self.last_call[0])
        v = int(self.last_call[2])
        actual_num = 0
        for num in the_dice_list:
            if num == v:
                actual_num += 1
        if self.last_pl_to_call == "user":
            if d > actual_num:
                round_winner = "robot"
                return round_winner
            else:
                round_winner = "user"
                return round_winner
        if self.last_pl_to_call == "robot":
            if d > actual_num:
                round_winner = "user"
                return round_winner
            else:
                round_winner = "robot"
                return round_winner

    def call(self):
        own_dice = self.dice_dict.get("robot_rolled")
        unknown_dice_quant = self.dice_quant_user
        if self.last_pl_to_call == "default" or self.last_pl_to_call == "robot":
            generated_nums = []
            for num in range(unknown_dice_quant):
                generated_nums.append(random.randint(1, 6))
            unreal_sum_dice = own_dice + generated_nums
            list_of_strings = [str(number) for number in unreal_sum_dice]
            string_num_dice = "".join(list_of_strings)                
            most_common = collections.Counter(string_num_dice).most_common(1) 
            return f"{most_common[0][1]}x{most_common[0][0]}"  

        if self.last_pl_to_call == "user":
            generated_nums = []
            for num in range(unknown_dice_quant):
                generated_nums.append(random.randint(1, 6))
            unreal_sum_dice = own_dice + generated_nums
            list_of_strings = [str(number) for number in unreal_sum_dice]
            string_num_dice = "".join(list_of_strings) 
            most_common = collections.Counter(string_num_dice).most_common(1)
            high_posibility = f"{most_common[0][1]}x{most_common[0][0]}"  
            if int(most_common[0][1]) > int(self.last_call[0]) and int(most_common[0][0]) >= int(self.last_call[2]): 
                return high_posibility
            if int(most_common[0][1]) >= int(self.last_call[0]) and int(most_common[0][0]) > int(self.last_call[2]):
                return high_posibility
            if int(most_common[0][1]) < int(self.last_call[0]) and int(most_common[0][0]) < int(self.last_call[2]):
                return "liar"
            if int(most_common[0][1]) > int(self.last_call[0]) and int(most_common[0][0]) < int(self.last_call[2]):
                return "liar"
            if int(most_common[0][1]) < int(self.last_call[0]) and int(most_common[0][0]) >= int(self.last_call[2]):
                return "liar"
            
    def game_winner(self):
        if self.dice_quant_user == 0:
            return "robot"
        elif self.dice_quant_robot == 0:
            return "user"



def main():
    if input("Hi and wellcome to my Liar's Dice. Would you like to read the rules of the game first? yes/no: ") == "yes":
        print("The game is played over multiple rounds. The first player for the first round is determined by rock, paper, scissors.\nTo begin each round, all players roll their dice simultaneously. Each player looks at their own dice after they roll, keeping them hidden from the other players.\nThe first player then states a bid consisting of a face and a quantity - e.g. 2x5, two dice of fives. The quantity represents the players guess as to how many of each face have been rolled by all the players, including themselves.\nEach subsequent player can either then make a higher bid of the same face - e.g 3x5 -, or they can call the previous player a liar. A player may bid a higher quantity of the same face - e.g 3x5 -, or the same quantity of a higher face - e.g. 2x6.\nIf liar is called, all players reveal their dice. If the bid is matched or exceeded, the bidder wins. Otherwise the challenger wins. The losing player of the round loses 1 die. The loser of the previous round begins the next round.\n")
        print("##########################################\n")
        
    winner_of_RPS = start_RPS() 
    connector = Connector(first_to_call = winner_of_RPS)
    temp_dict_dice_to_list = {}

    while connector.dice_quant() == True:
        dice_dictionary = dice_roller(connector.dice_count())
        temp_dict_dice_to_list = dice_dictionary.get("user_rolled") + dice_dictionary.get("robot_rolled") 
        connector.update_dice_dict(dice_dictionary)
        if connector.first_to_call == "user":
            loopend = False
            while loopend == False:  
                user_is_done = False
                robot_is_done = False
                while user_is_done == False:
                    try:
                        user_input = input("Say a 'call' or 'liar'?: ")
                        if user_input == "call":
                            call_input = input("Tell me the call as 'dice count'x'face value'. Example: 3x4 : ")
                            if connector.call_validator(call_input) == False:
                                raise ValueError
                            user_is_done = True
                            connector.update_last_call(call_input)
                            connector.update_last_pl_to_call("user")
                        if user_input == "liar":
                            if (connector.give_last_pl_to_call() == "default" or connector.last_call == "0x0"):
                                print("Something is yet to be called. Please call.")
                                raise ValueError
                            user_is_done = True
                            robot_is_done = True
                            loopend = True
                    except ValueError:
                        user_is_done = False
                while robot_is_done == False:
                    robot_call = connector.call()
                    if str(robot_call)[1] == "x":
                        try:
                            if connector.call_validator(robot_call) == False:
                                raise ValueError
                            print(f"I call: {robot_call}")
                            connector.update_last_call(robot_call)
                            connector.update_last_pl_to_call("robot")
                            user_is_done = False
                            robot_is_done = True
                        except ValueError:
                            robot_is_done = False                      
                    if robot_call == "liar":
                        print("Liar!")
                        user_is_done = True
                        robot_is_done = True
                        loopend = True

        

        if connector.first_to_call == "robot":
            loopend = False
            while loopend == False:
                user_is_done = False
                robot_is_done = False
                while robot_is_done == False:
                    robot_call = connector.call()
                    if str(robot_call)[1] == "x":
                        try:
                            if connector.call_validator(robot_call) == False:
                                raise ValueError
                            print(f"I call: {robot_call}")
                            connector.update_last_call(robot_call)
                            connector.update_last_pl_to_call("robot") 
                            user_is_done = False
                            robot_is_done = True
                        except ValueError:
                            robot_is_done = False
                    if robot_call == "liar":
                        print("Liar!")
                        user_is_done = True
                        robot_is_done = True
                        loopend = True
                while user_is_done == False:
                    try:
                        user_input = input("Say a 'call' or 'liar'?: ")
                        if user_input == "call":
                            call_input = input("Tell me the call as 'dice count'x'face value'. Example: 3x4 : ")
                            if connector.call_validator(call_input) == False:
                                raise ValueError
                            user_is_done = True
                            connector.update_last_call(call_input)
                            connector.update_last_pl_to_call("user")
                        if user_input == "liar":
                            if (connector.give_last_pl_to_call() == "default" or connector.last_call == "0x0"):
                                print("Something is yet to be called. Please call.")
                                raise ValueError
                            user_is_done = True
                            robot_is_done = True
                            loopend = True
                    except ValueError:
                        user_is_done = False

        temp_to_print = ""
        for i in temp_dict_dice_to_list:
            temp_to_print += str(i)
        print("Dice pool: " + temp_to_print)

        round_winner = connector.checker()
        score = score_updater(round_winner, connector.dice_count())  
        if score[0] == "user":
            connector.reduce_user_dice(score[1])
            print("I win this round. :)")     
        if score[0] == "robot":
            connector.reduce_robot_dice(score[1])
            print("You won the round!")

        connector.update_first_to_call(round_winner)
        connector.last_call = "0x0"
        print("#######################################")
        print()

    winner_temp = connector.game_winner()
    if winner_temp == "user":
        print("The winner of the game is You. :)")
    elif winner_temp == "robot":
        print("I am the winner of the game.")

    print("The End.")
    quit()


def start_RPS():
    i = True
    while i == True:
        value = random.randint(1,3)
        if value == 1:
            robot_RPS = "rock"
        elif value == 2:
            robot_RPS = "paper"
        else:
            robot_RPS = "scissors"
        user_RPS = input('Please choose "rock","paper" or "scissors" as written here: ').strip().lower()

        if user_RPS == "rock" and robot_RPS == "rock":
            print("Rock and rock. Its a tie! Go again.")
            pass
        elif user_RPS == "rock" and robot_RPS == "paper":
            print("Paper! I win.")
            winner = "robot"
            i = False
            break
        elif user_RPS == "rock" and robot_RPS == "scissors":
            print("Scissors... you win.")
            winner = "user"
            i = False
            break

        elif user_RPS == "paper" and robot_RPS == "rock":
            print("Rock... you win.")
            winner = "user"
            i = False
            break
        elif user_RPS == "paper" and robot_RPS == "paper":
            print("Paper and paper. Its a tie! Go again.")
            pass
        elif user_RPS == "paper" and robot_RPS == "scissors":
            print("Scissors! I win.")
            winner = "robot"
            i = False
            break

        elif user_RPS == "scissors" and robot_RPS == "rock":
            print("Rock! I win.")
            winner = "robot"
            i = False
            break
        elif user_RPS == "scissors" and robot_RPS == "paper":
            print("Paper... you win.")
            winner = "user"
            i = False
            break
        elif user_RPS == "scissors" and robot_RPS == "scissors":
            print("Scissors and scissors. Its a tie! Go again.")
            pass


    return winner


def dice_roller(dice_count):
    user_dice_count, robot_dice_count = dice_count.get("user"), dice_count.get("robot")
    user_rolled_dice = []
    robot_rolled_dice = []
    for i in range(int(user_dice_count)):
        num = random.randint(1, 6)
        user_rolled_dice.append(num)
    for i in range(int(robot_dice_count)):
        num = random.randint(1, 6)
        robot_rolled_dice.append(num)
    print(f"User roll: {user_rolled_dice}. Robot dice count: {int(robot_dice_count)}")
    return {"user_rolled":list(user_rolled_dice), "robot_rolled":list(robot_rolled_dice)}



def score_updater(round_winner, dice_count):
    if round_winner == "robot":
        _dice_count = dice_count
        user_dice_count = _dice_count.get("user")
        new_dice_quant_user = (int(user_dice_count) - 1)
        return ["user", new_dice_quant_user]
    if round_winner == "user":
        _dice_count = dice_count
        robot_dice_count = _dice_count.get("robot")
        new_dice_quant_robot = (int(robot_dice_count) - 1)
        return ["robot", new_dice_quant_robot]


if __name__ == "__main__":
    main()
