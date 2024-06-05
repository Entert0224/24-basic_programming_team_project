from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9, Team, TotalGameResult
from random import sample 

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class GameScene(Scene) :
    cell_button : list = []
    game_background : Sprite = None
    #game_list : list[Scene] = sample([Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9], 9)
    game_list : list[Scene] = [Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9]

    notice_panal = None
    notice_text = None
    check_text = None
    check_button = None
    next_text = None
    next_button = None

    previous_game_index = 0
    played_game_results = dict()

    Tic_Tac_Toe_baord = [['','',''] for _ in range(3)]


    @classmethod
    def JudgeWinner(cls) :
        if not Team.is_playing : return

        Team.is_playing = False

        odd_sign = Team.ODD_TEAM_SIGN
        even_sign = Team.EVEN_TEAM_SIGN
        winner_sign = odd_sign if Team.JudgeWinner() == odd_sign else even_sign
        cls.played_game_results[cls.previous_game_index] = winner_sign

    @classmethod
    def CheckLine(cls):
        board = cls.Tic_Tac_Toe_baord
        # 가로 체크
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != '':
                return row[0]
        
        # 세로 체크
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
                return board[0][col]
        
        # 대각선 체크
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return board[0][0]
        
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return board[0][2]
        
        # 승자가 없을 경우
        return 'OX'


    @classmethod
    def Setup(cls) :
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)

        cls.JudgeWinner()

        Team.Set_current_team_turn(Team.Get_current_team_turn() + 1)
        cls.game_background = Sprite("assets/images/GameScene.jpg", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        for i in range(3) :
            for j in range(3) :
                idx = 3 * i + j 
                x = SCREEN_WIDTH / 2 + (135 * (j - 1))
                y = SCREEN_HEIGHT / 2 + 8 + (135 * (i - 1))

                ksprite = None
                if idx in cls.played_game_results :
                    ox_sign = cls.played_game_results[idx]
                    ksprite = Sprite(f"assets/images/{ox_sign}.png", Vec2(x, y), color=pygame.Color(255,255,255,255))
                    cls.Tic_Tac_Toe_baord[i][j] = ox_sign
                else :
                    ksprite = Sprite("assets/images/OX.png", Vec2(x, y), color=pygame.Color(255,255,255,0))
                
                cls.cell_button.append(ksprite.CreateButton())
        
        cls.notice_panal = Sprite("assets/images/end_panal.png", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), layer=10, visible=False) 
        cls.notice_text = Text("",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60),size=30 ,layer=11, fontpath="assets/fonts/H2HDRM.TTF")
        cls.check_text = Sprite("assets/images/check.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150),scale=Vec2(0.9,0.9),layer=11, visible=False)
        cls.check_button = cls.check_text.CreateButton()

        if not cls.CheckLine() == 'OX' :
            cls.notice_panal.visible = True
            cls.check_text.visible = True

            if cls.CheckLine() == Team.ODD_TEAM_SIGN :
                Team.MakeLine(True)
                cls.notice_text.SetString("홀수 팀이 한 줄을 완성 했어요!\n홀수 팀 모두 300점 획득")
            else :
                Team.MakeLine(False)
                cls.notice_text.SetString("짝수 팀이 한 줄을 완성 했어요!\n짝수 팀 모두 300점 획득")

        cur_team_number_text = Text(f"{Team.Get_current_team_turn()}팀 차례", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250), size=50 , fontpath="assets/fonts/H2HDRM.TTF")

        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 154 - 35), 35, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = "-현재 점수-"
        for idx, score in enumerate(Team.entire_game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:04d}"

        display_scores_text_ins.SetString(display_scores_text)

        cls.next_text = Sprite("assets/images/next_text.png",Vec2(700,560),scale=Vec2(1.53,1.53),layer=1, visible=False, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()
        if len(cls.played_game_results) >= 9 :
            cls.next_text.visible = True

    @classmethod
    def Update(cls) :
        for idx, cell_sprite in enumerate(cls.cell_button) :
            if idx in cls.played_game_results : continue

            if cell_sprite(color_effect = pygame.Color(255,255,255,255)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    Team.is_playing = True
                    cls.previous_game_index = idx
                    cls.played_game_results[idx] = None
                    Director.ChangeScene(cls.game_list[idx])
                    break

        if cls.check_text.visible :
            if cls.check_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    cls.notice_panal.visible = False
                    cls.check_text.visible = False
                    cls.notice_text.SetString("")

        if cls.next_text.visible :
            if cls.next_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    Director.ChangeScene(TotalGameResult)

    @classmethod
    def Exit(cls) :
        cls.cell_button.clear()
        Team.game_score = [0 for _ in range(Team.Get_team_number_count())]

