class Team :
    EVEN_TEAM_SIGN = "O"
    ODD_TEAM_SIGN = "X"

    __team_number_count : int = 2
    __current_team_turn : int = 1

    is_playing = False
    game_score = dict()
    entire_game_score = list()

    @classmethod
    def Set_team_number_count(cls, value: int):
        cls.__team_number_count = max(2, min(value, 9))

    @classmethod
    def Get_team_number_count(cls) :
        return cls.__team_number_count
    

    @classmethod
    def Set_current_team_turn(cls, value: int):
        cls.__current_team_turn = 1 + (value - 1) % cls.Get_team_number_count()#max(1, min(value, cls.Get_team_number_count()))

    @classmethod
    def Get_current_team_turn(cls) :
        return cls.__current_team_turn
    

    @classmethod
    def JudgeWinner(cls) :
        max_value = max(cls.game_score)
        winner_team_num = [i + 1 for i, x in enumerate(cls.game_score) if x == max_value]

        if all(i % 2 == 0 for i in winner_team_num):
            return cls.EVEN_TEAM_SIGN
        elif all(i % 2 != 0 for i in winner_team_num):
            return cls.ODD_TEAM_SIGN
        else:
            return cls.EVEN_TEAM_SIGN if cls.Get_current_team_turn() % 2 == 0 else cls.ODD_TEAM_SIGN
        
