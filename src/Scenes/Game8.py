from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time, Sound
from Scenes import Team
from random import randint

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#여덟번째 미니게임 Scene
#버튼 많이 클릭하기 게임
class Game8(Scene) :
    click_count = 0

    team_number = 1
    timer = 15
    scores = []
    countdown_number = 4
    is_first_game = True

    is_ready = True
    is_countdown = True
    is_end = False

    start_button = None
    ready_panal = None
    start_text = None
    countdown_text = None
    timer_text = None
    click_sprite = None
    click_button = None
    score_text = None
    next_text = None
    next_button = None
    end_panal = None

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        if cls.is_first_game :
            cls.is_first_game = False
            cls.scores = [0 for i in range(0, Team.Get_team_number_count())]
            cls.desc_panal = Sprite("assets/images/Desc_Click.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), layer=13)
            cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 175),layer=14,color=pygame.Color(0,0,0,255))
        else :
            cls.desc_panal = Sprite("assets/images/Desc_Click.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), layer=13, visible = False)
            cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),layer=14)

        #배경 및 AI 마크
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        
        #준비
        team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_button = cls.start_text.CreateButton()

        #시작 전 카운트 다운
        cls.countdown_text = Text(f"3",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 100),90,layer=5,visible=False,fontpath="assets/fonts/H2HDRM.TTF")
        
        #타이머와 클릭 버튼
        cls.timer_text = Text(f"{cls.timer:.2f}",Vec2(SCREEN_WIDTH/2 - 340, SCREEN_HEIGHT/2 - 270), size=45, fontpath="assets/fonts/H2HDRM.TTF") 
        cls.click_sprite = Sprite("assets/images/click_btn.png", Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        cls.click_button = cls.click_sprite.CreateButton()

         #끝난 후 그 팀 결과
        cls.end_panal = Sprite("assets/images/end_panal.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 19), layer = 19, visible = False)
        cls.score_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()

    #준비
    @classmethod
    def Ready(cls) :
        if cls.start_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() : #시작 버튼을 눌렀을 시
                Sound.PlaySound("click")
                cls.desc_panal.visible = False
                cls.is_ready = False
                cls.ready_panal.visible = False
                cls.start_text.visible = False
                cls.countdown_text.visible = True

    #게임 시작전 카운트 다운
    @classmethod
    def CountDown(cls) :
        cls.countdown_number -= Time.GetDeltaTime()
        if cls.countdown_number >= 3 :
            cls.countdown_text.SetString("3")
        elif cls.countdown_number >= 2 :
            cls.countdown_text.SetString("2")
        elif cls.countdown_number >= 1 :
            cls.countdown_text.SetString("1")
        elif cls.countdown_number >= 0 :
            cls.countdown_text.SetString("Start")
        elif cls.countdown_number < 0 :
            cls.countdown_text.visible = False
            cls.is_countdown = False

    #게임 시작
    @classmethod
    def Start(cls) :
        cls.timer -= Time.GetDeltaTime()
        if cls.timer < 0 : # 타임오버
            cls.timer = 0
            cls.is_end = True
        cls.timer_text.SetString(f"{cls.timer:.2f}") #시간 텍스트 설정

        if cls.click_button(Vec2(1.1,1.1)) :
            if Mouse.isDown() : #버튼을 누를 떄마다
                Sound.PlaySound("click")
                cls.scores[cls.team_number - 1] += 1 #미니게임 점수 1점씩 추가
            elif Mouse.isHold() : #버튼 효과
                cls.click_sprite.rotation = randint(-7,7)
                cls.click_sprite.color = pygame.Color(220,220,220,255)
            else :
                cls.click_sprite.rotation = 0
                cls.click_sprite.color = pygame.Color(255,255,255,255)
    
    #게임 끝
    @classmethod
    def End(cls) :
        cls.click_sprite.rotation = 0
        cls.click_sprite.color = pygame.Color(255,255,255,255)

        cls.ready_panal.visible = True
        cls.end_panal.visible = True
        cls.score_text.visible = True

        #점수 세팅
        cur_team_score = cls.scores[cls.team_number - 1]
        cls.score_text.SetString(f"점수 : {cur_team_score}")

        Team.game_score[cls.team_number - 1] = cur_team_score

        #모든 팀이 끝났을 경우
        if cls.team_number >= Team.Get_team_number_count() :
            cls.next_text.visible = True
            if cls.next_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    Team.GamescoreGrading()
                    from Scenes import MiniGameResult
                    Director.ChangeScene(MiniGameResult)
        else : #모든 팀이 끝나지 않은 경우
            cls.next_text.visible = True
            if cls.next_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    Sound.PlaySound("click")
                    Director.ChangeScene(cls)

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        if cls.is_ready :
            cls.Ready()
            return

        if cls.is_countdown :
            cls.CountDown()
            return 

        if not cls.is_end :    
            cls.Start()
        else :
            cls.End()

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        cls.click_count = 0

        cls.team_number += 1
        cls.timer = 15
        cls.countdown_number = 4

        cls.is_ready = True
        cls.is_countdown = True
        cls.is_end = False