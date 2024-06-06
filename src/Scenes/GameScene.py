from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9, Team, TotalGameResult
from random import sample 

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height
#티택토가 있는 게임 Scene
#미니게임을 선택하는 Scene
class GameScene(Scene) :
    cell_button : list = []
    #1~9번째 게임을 랜덤으로 섞는다.
    game_list : list[Scene] = sample([Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9], 9)
    #game_list : list[Scene] = [Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9]

    notice_panal = None
    notice_text = None
    check_text = None
    check_button = None
    next_text = None
    next_button = None

    previous_game_index = 0
    played_game_results = dict()

    #티택토 줄 감지 및 중복 방지
    Tic_Tac_Toe_baord = [['', '', ''] for _ in range(3)]
    duplicate_check = [[False, False, False] for _ in range(3)]

    #전 미니게임에서 이긴 팀 결정
    @classmethod
    def JudgeWinner(cls) :
        if not Team.is_playing : return

        Team.is_playing = False

        odd_sign = Team.ODD_TEAM_SIGN
        even_sign = Team.EVEN_TEAM_SIGN
        winner_sign = odd_sign if Team.JudgeWinner() == odd_sign else even_sign
        cls.played_game_results[cls.previous_game_index] = winner_sign

    #틱택토 한 줄을 만들었는지 검사
    @classmethod
    def CheckLine(cls):
        board = cls.Tic_Tac_Toe_baord
        # 가로 체크
        for idx, row in enumerate(board):
            if row[0] == row[1] == row[2] and row[0] != '':
                if all([cls.duplicate_check[idx][i] for i in range(3)]) : continue
                for i in range(3) :
                    cls.duplicate_check[idx][i] = True
                return row[0]
        
        # 세로 체크
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
                if all([cls.duplicate_check[i][col] for i in range(3)]) : continue
                for i in range(3) :
                    cls.duplicate_check[i][col] = True
                return board[0][col]
        
        # 대각선 체크
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            if not all([cls.duplicate_check[i][i] for i in range(3)]) :
                for i in range(3) :
                    cls.duplicate_check[i][i] = True
                return board[0][0]
        
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            if not all([cls.duplicate_check[i][2 - i] for i in range(3)]) :
                for i in range(3) :
                    cls.duplicate_check[i][2 - i] = True
                return board[0][2]
        
        # 승자가 없을 경우
        return 'OX'

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
         #배경 및 AI 마크
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        game_background = Sprite("assets/images/GameScene.jpg", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        
        #전 판 미니게임 승부를 판단한다.
        cls.JudgeWinner()

        #현재 팀의 차례를 설정한다.
        Team.Set_current_team_turn(Team.Get_current_team_turn() + 1)

        #틱택토 칸을 업데이트한다.
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
        
        #알림 창
        cls.notice_panal = Sprite("assets/images/end_panal.png", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), layer=10, visible=False) 
        cls.notice_text = Text("",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80),size=30 ,layer=11, fontpath="assets/fonts/H2HDRM.TTF")
        cls.check_text = Sprite("assets/images/check.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 130),scale=Vec2(0.7,0.7),layer=11, visible=False)
        cls.check_button = cls.check_text.CreateButton()
        
        #티택토 줄이 만들어졌는지 검사 및 알림
        result = cls.CheckLine()
        if not result == 'OX' :
            cls.notice_panal.visible = True
            cls.check_text.visible = True

            if result == Team.ODD_TEAM_SIGN :
                Team.MakeLine(True)
                cls.notice_text.SetString("홀수 팀이 한 줄을 완성 했어요!\n홀수 팀 모두 300점 획득")
            else :
                Team.MakeLine(False)
                cls.notice_text.SetString("짝수 팀이 한 줄을 완성 했어요!\n짝수 팀 모두 300점 획득")

        #어떤 팀의 차례인지 보여주기 위한 텍스트
        cur_team_number_text = Text(f"{Team.Get_current_team_turn()}팀 차례", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250), size=50 , fontpath="assets/fonts/H2HDRM.TTF")

        #옆 사이드 바에 모든 팀의 현재 점수를 보여주기 위한 코드
        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 154 - 35), 35, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = "-현재 점수-"
        for idx, score in enumerate(Team.entire_game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:04d}"

        display_scores_text_ins.SetString(display_scores_text)

        #티택토의 모든 게임이 마무리가 되고 나타나는 최종 결과 창으로 이동하는 다음 버튼
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(700,560),scale=Vec2(1.53,1.53),layer=1, visible=False, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()
        if len(cls.played_game_results) >= 9 :
            cls.next_text.visible = True

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        if cls.check_text.visible : #알림창이 떳을 경우
            if cls.check_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() : #확인 누르면 닫힘
                    Sound.PlaySound("click")
                    cls.notice_panal.visible = False
                    cls.check_text.visible = False
                    cls.notice_text.SetString("")
            return

        #티택토 각 칸마다의 버튼 감지
        for idx, cell_sprite in enumerate(cls.cell_button) :
            if idx in cls.played_game_results : continue #이미 했던 게임은 선택 불가

            if cell_sprite(color_effect = pygame.Color(255,255,255,255)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    Team.is_playing = True
                    cls.previous_game_index = idx
                    cls.played_game_results[idx] = None
                    Director.ChangeScene(cls.game_list[idx])
                    break

        #최종 결과 화면으로 가기 위한 버튼이 떳을 시
        if cls.next_text.visible :
            if cls.next_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() : #누르면
                    Sound.PlaySound("click")
                    Director.ChangeScene(TotalGameResult) #최종 결과 화면으로 이동

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        cls.cell_button.clear()
        Team.game_score = [0 for _ in range(Team.Get_team_number_count())] #미니게임 스코어 초기화

