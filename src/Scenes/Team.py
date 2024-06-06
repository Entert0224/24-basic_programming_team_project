#Team을 관리하는 클래스
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

    #참가한 팀 수 설정
    @classmethod
    def Set_team_number_count(cls, value: int):
        cls.__team_number_count = max(2, min(value, 9))

    #참가한 팀 수 가져오기
    @classmethod
    def Get_team_number_count(cls) :
        return cls.__team_number_count
    
    #현재 어떤 팀의 차레인지 설정
    @classmethod
    def Set_current_team_turn(cls, value: int):
        cls.__current_team_turn = 1 + (value - 1) % cls.Get_team_number_count()

    #차례 가져오기
    @classmethod
    def Get_current_team_turn(cls) :
        return cls.__current_team_turn
    
    #틱택토 한 줄 완성 했는가
    @classmethod
    def MakeLine(cls, isOdd : bool) :
        num = 1 if isOdd else 0
        for idx in range(cls.Get_team_number_count()) :
            if (idx + 1) % 2 == num :
                cls.entire_game_score[idx] += 300

    # 미니게임 등수 매기고 최종 점수에 반영
    @classmethod
    def GamescoreGrading(cls):
        sorted_score = sorted(cls.game_score, reverse=True)

        rank =[] # 등수
        for i in cls.game_score:
            # index는 맨 앞에 위치한 요소의 인덱스 번호를 리턴
            rank.append(sorted_score.index(i) + 1) 

        #1등 100, 2등 80, 3등 50
        for idx, i in enumerate(rank) :
            if i == 1 :
                cls.entire_game_score[idx] += 100
            elif i == 2 :
                cls.entire_game_score[idx] += 80
            elif i == 3 :
                cls.entire_game_score[idx] += 50

        cls.game_score_rank = rank[:]
                
   # 최종 등수 매기기
    @classmethod
    def TotalGamescoreGrading(cls):
        sorted_score = sorted(cls.entire_game_score, reverse=True)

        rank =[] # 등수
        for i in cls.entire_game_score:
            rank.append(sorted_score.index(i) + 1)

        cls.entire_game_score_rank = rank[:]

    #미니게임 판 승리 팀 판정
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
        
