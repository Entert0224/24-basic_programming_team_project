class Team :
    EVEN_TEAM_SIGN = "O"
    ODD_TEAM_SIGN = "X"

    __team_number_count : int = 2
    __current_team_turn : int = 0

    is_playing = False
    game_score = list()
    game_score_rank = list() 
    entire_game_score = list()
    entire_game_score_rank = list() 

    @classmethod
    def Set_team_number_count(cls, value: int):
        cls.__team_number_count = max(2, min(value, 9))

    @classmethod
    def Get_team_number_count(cls) :
        return cls.__team_number_count
    

    @classmethod
    def Set_current_team_turn(cls, value: int):
        cls.__current_team_turn = 1 + (value - 1) % cls.Get_team_number_count()

    @classmethod
    def Get_current_team_turn(cls) :
        return cls.__current_team_turn
    
    @classmethod
    def MakeLine(cls, isOdd : bool) :
        num = 1 if isOdd else 0
        for idx in range(cls.Get_team_number_count()) :
            if (idx + 1) % 2 == num :
                cls.entire_game_score[idx] += 300

    # 동점자 처리 함수
    @classmethod
    def GamescoreGrading(cls):
        sorted_score = sorted(cls.game_score, reverse=True)

        rank =[] # 등수
        for i in cls.game_score:
            rank.append(sorted_score.index(i) + 1) # index는 맨 앞에 위치한 요소의 인덱스 번호를 리턴

        for idx, i in enumerate(rank) :
            if i == 1 :
                cls.entire_game_score[idx] += 100
            elif i == 2 :
                cls.entire_game_score[idx] += 80
            elif i == 3 :
                cls.entire_game_score[idx] += 50

        cls.game_score_rank = rank[:]
                
    # 동점자 처리 함수
    @classmethod
    def TotalGamescoreGrading(cls):
        sorted_score = sorted(cls.entire_game_score, reverse=True)

        rank =[] # 등수
        for i in cls.entire_game_score:
            rank.append(sorted_score.index(i) + 1)

        cls.entire_game_score_rank = rank[:]

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
        
