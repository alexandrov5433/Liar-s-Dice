from project import score_updater, dice_roller, start_RPS, Connector
import mock

def main():
    test_score_updater()
    test_dice_roller()
    test_start_RPS()
    test_call()
    test_checker()
    test_call_validatior()
    test_dice_count()

def test_score_updater():
    assert score_updater("user" ,{"user": 5, "robot": 5}) == ["robot", 4]
    assert score_updater("robot" ,{"user": 5, "robot": 5}) == ["user", 4]

def test_dice_roller():
    temp_dict = dice_roller({"user": 5, "robot": 5})
    assert len(temp_dict.get("user_rolled")) == 5
    assert len(temp_dict.get("robot_rolled")) == 5

    temp_dict_2 = dice_roller({"user": 3, "robot": 2})
    assert len(temp_dict_2.get("user_rolled")) == 3
    assert len(temp_dict_2.get("robot_rolled")) == 2

def test_start_RPS():
    input_patch = mock.patch("builtins.input", return_value = "rock")
    randint_patch = mock.patch("random.randint", return_value = 3)
    
    input_patch.start()
    randint_patch.start()
    assert start_RPS() == "user"
    
    randint_patch.stop()
    randint_patch = mock.patch("random.randint", return_value = 2)
    randint_patch.start()
    assert start_RPS() == "robot"

    input_patch.stop()
    randint_patch.stop()
   
def test_call():
    con = Connector()
    con.dice_dict = {"user_rolled":[1,4,3,4,6], "robot_rolled":[3,2,4,1,1]}
    con.dice_quant_user = 5
    con.last_pl_to_call = "robot"
    temp_call = con.call()
    assert isinstance(temp_call, str) == True
    assert isinstance(int(temp_call[0]), int) == True
    assert temp_call[1] == "x"
    assert isinstance(int(temp_call[2]), int) == True

def test_checker():
    con = Connector()
    con.dice_dict = {"user_rolled":[1,4,3,4,6], "robot_rolled":[3,2,4,1,1]}
    con.last_pl_to_call = "robot"
    con.last_call = "2x4"
    temp_checker = con.checker()
    assert temp_checker == "robot"

    con.last_pl_to_call = "user"
    temp_checker_2 = con.checker()
    assert temp_checker_2 == "user"

def test_call_validatior():
    con = Connector()
    con.last_call = "3x4"
    assert con.call_validator("3x4") == False
    assert con.call_validator("4x4") == True
    assert con.call_validator("4x5") == True
    assert con.call_validator("3x3") == False
    assert con.call_validator("4x3") == False
    assert con.call_validator("0x0") == False
    assert con.call_validator("x") == False
    assert con.call_validator("X") == False
    assert con.call_validator("") == False

def test_dice_count():
    con = Connector()
    con.dice_quant_user = 5
    con.dice_quant_robot = 5
    assert con.dice_count() == {"user":5, "robot":5}

if __name__ == "__main__":
    main()