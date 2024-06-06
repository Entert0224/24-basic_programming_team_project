from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team
from random import randint

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#세번째 미니게임 Scene
#난수 맞추기 미니게임
class Game3(Scene) :
    team_number = 1
    scores = []

    answer_number = 0

    input_content = ""

    is_ready = True
    is_end = False

    desc_panal = None
    team_number_text = None
    start_button = None
    input_box = None
    input_text = None
    ready_panal = None
    start_text = None
    back_text = None
    next_button = None
    back_button = None
    end_panal = None
    display_scores_text = None
    display_result_text = None

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        #게임에 필요한 정보 설정
        cls.desc_panal = Sprite("assets/images/Desc_random_number.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), layer= 13)
        cls.scores = [0 for i in range(0, Team.Get_team_number_count())]
        cls.answer_number = randint(0, 999)

        #배경 및 AI 마크
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        
        #준비
        cls.team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 175),layer=14,color=pygame.Color(0,0,0,255))
        cls.start_button = cls.start_text.CreateButton()

        #키보드 입력을 받을 텍스트와 이미지
        cls.input_box = Sprite("assets/images/input_box.png", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        cls.input_text = Text("", Vec2(SCREEN_WIDTH/2 + 30, SCREEN_HEIGHT/2), 39, layer = 2, fontpath="assets/fonts/H2HDRM.TTF")

        #다음 팀으로 넘어가는 next 그림
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), layer=10, color=pygame.Color(0,0,0,150))
        
        #끝난 후 결과
        cls.end_panal = Sprite("assets/images/end_panal.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 19),scale=Vec2(0.7,1), layer = 19, visible = False)
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 145), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.back_button = cls.back_text.CreateButton()
        cls.display_scores_text = Text("",Vec2(SCREEN_WIDTH/2 - 293, SCREEN_HEIGHT/2 - 154),38,layer=21, visible=False,fontpath="assets/fonts/H2HDRM.TTF")
        cls.display_result_text = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 95),50,30,False,fontpath="assets/fonts/H2HDRM.TTF")

    #준비
    @classmethod
    def Ready(cls) :
        if cls.start_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                cls.desc_panal.visible = False
                cls.is_ready = False
                cls.ready_panal.visible = False
                cls.start_text.visible = False

    #키 입력을 받는다.
    @classmethod
    def Event(cls) :
        input_text = cls.input_content
        for event in Director.event_list:

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                if len(input_text) >= 3 : continue
                
                if event.key == pygame.K_0:
                    input_text += '0'
                elif event.key == pygame.K_1:
                    input_text += '1'
                elif event.key == pygame.K_2:
                    input_text += '2'
                elif event.key == pygame.K_3:
                    input_text += '3'
                elif event.key == pygame.K_4:
                    input_text += '4'
                elif event.key == pygame.K_5:
                    input_text += '5'
                elif event.key == pygame.K_6:
                    input_text += '6'
                elif event.key == pygame.K_7:
                    input_text += '7'
                elif event.key == pygame.K_8:
                    input_text += '8'
                elif event.key == pygame.K_9:
                    input_text += '9'
                
                cls.input_content = input_text
                
        cls.input_text.SetString(str(cls.input_content))

    #게임 시작
    @classmethod
    def Start(cls) : 
        #next 이미지를 텍스트 입력 여부에 따라 활성화 및 비활성화
        if cls.input_content :
            cls.next_text.color.a = 255
            if cls.next_text.PointInRect(Mouse.GetMousePos()):
                cls.next_text.scale = Vec2(1.2,1.2)
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    cls.scores[cls.team_number - 1] = int(cls.input_content)
                    cls.team_number += 1
                    cls.input_content = ""
                    if cls.team_number > Team.Get_team_number_count() :
                        cls.is_end = True
                        return

                    cls.team_number_text.SetString(f"{str(cls.team_number)} 팀")
                    
            else :
                cls.next_text.scale = Vec2(1, 1)
        else :
            cls.next_text.color.a = 150
            cls.next_text.scale = Vec2(1, 1)

    #게임 끝
    @classmethod
    def End(cls) :
        if cls.back_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Team.GamescoreGrading()
                from Scenes import GameScene
                Director.ChangeScene(GameScene)

        if cls.ready_panal.visible == True : return

        #최종 결과를 보여준다.
        cls.next_text.visible = False
        cls.ready_panal.visible = True
        cls.display_scores_text.visible =True
        cls.back_text.visible = True
        cls.end_panal.visible = True
        cls.display_result_text.visible = True

        #점수 세팅
        display_scores_text = "선택한 숫자"
        for idx, score in enumerate(cls.scores) :
            display_scores_text += f"\n{idx + 1}팀 : {score:03d}"

            distance_score_answer = abs(cls.answer_number - score)
            cls.scores[idx] = distance_score_answer
            Team.game_score[idx] = 999 - distance_score_answer
        cls.display_scores_text.SetString(display_scores_text)

        #승부 결과
        is_draw = True if cls.scores.count(min(cls.scores)) > 1 else False
        if is_draw :
            winner_teams = "홀" if Team.Get_current_team_turn() % 2 == 1 else "짝"
            cls.display_result_text.SetString(f"결과\n답 : {cls.answer_number}\n무승부\n{winner_teams}수 팀 승")
        else :
            winner_team = cls.scores.index(min(cls.scores)) + 1
            winner_teams = "홀" if winner_team % 2 == 1 else "짝"
            cls.display_result_text.SetString(f"결과\n답 : {cls.answer_number}\n{winner_team}팀 승\n{winner_teams}수 팀 승")

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        if cls.is_ready :
            cls.Ready()
            return

        if not cls.is_end :    
            cls.Event()
            cls.Start()
        else :
            cls.End()

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        cls.is_ready = True
        cls.is_end = False