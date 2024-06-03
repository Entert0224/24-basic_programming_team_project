from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time
from Scenes import Team
from random import randint

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class Game8(Scene) :
    click_count = 0

    team_number = 1
    timer = 1
    scores = [0 for i in range(0, Team.Get_team_number_count())]
    countdown_number = 4

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
    back_text = None
    next_button = None
    back_button = None
    end_panal = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),layer=11)
        cls.start_button = cls.start_text.CreateButton()

        cls.countdown_text = Text(f"3",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 100),90,layer=5,visible=False,fontpath="assets/fonts/H2HDRM.TTF")
        
        cls.timer_text = Text(f"{cls.timer:.2f}",Vec2(SCREEN_WIDTH/2 - 340, SCREEN_HEIGHT/2 - 270), size=45, fontpath="assets/fonts/H2HDRM.TTF") 
        cls.click_sprite = Sprite("assets/images/click_btn.png", Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        cls.click_button = cls.click_sprite.CreateButton()

        cls.end_panal = Sprite("assets/images/end_panal.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 19), layer = 19, visible = False)
        cls.score_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()
        cls.back_button = cls.back_text.CreateButton()

        
    @classmethod
    def Ready(cls) :
        if cls.start_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                cls.is_ready = False
                cls.ready_panal.visible = False
                cls.start_text.visible = False
                cls.countdown_text.visible = True

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

    @classmethod
    def Start(cls) :
        cls.timer -= Time.GetDeltaTime()
        if cls.timer < 0 :
            cls.timer = 0
            cls.is_end = True
        cls.timer_text.SetString(f"{cls.timer:.2f}")

        if cls.click_button(Vec2(1.1,1.1)) :
            if Mouse.isDown() :
                cls.scores[cls.team_number - 1] += 1
            elif Mouse.isHold() :
                cls.click_sprite.rotation = randint(-7,7)
                cls.click_sprite.color = pygame.Color(220,220,220,255)
            else :
                cls.click_sprite.rotation = 0
                cls.click_sprite.color = pygame.Color(255,255,255,255)
            
    @classmethod
    def End(cls) :
        cls.click_sprite.rotation = 0
        cls.click_sprite.color = pygame.Color(255,255,255,255)

        cls.ready_panal.visible = True
        cls.end_panal.visible = True
        cls.score_text.visible = True
        cur_team_score = cls.scores[cls.team_number - 1]
        cls.score_text.SetString(f"점수 : {cur_team_score}")

        Team.game_score[cls.team_number - 1] = cur_team_score

        if cls.team_number >= Team.Get_team_number_count() :
            cls.back_text.visible = True
            if cls.back_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    from Scenes import GameScene
                    Director.ChangeScene(GameScene)
        else :
            cls.next_text.visible = True
            if cls.next_button(Vec2(1.2,1.2)) :
                if Mouse.isDown() :
                    Director.ChangeScene(cls)

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

    @classmethod
    def Exit(cls) :
        cls.click_count = 0

        cls.team_number += 1
        cls.timer = 1
        cls.countdown_number = 4

        cls.is_ready = True
        cls.is_countdown = True
        cls.is_end = False



    
        #cls.click_text = Text(f"Clicks: {cls.click_count}", Vec2(SCREEN_WIDTH / 2, 100), 40, fontpath="assets/fonts/H2HDRM.TTF")

        # for i in range(Team.team_number_count):
        #     text = Text(f"Team {i + 1}: {Team.team_scores[i]}", Vec2(100, 50 + i * 40), 30, fontpath="assets/fonts/H2HDRM.TTF")
        #     cls.score_texts.append(text)

        # for i, text in enumerate(cls.score_texts):
        #     text.SetString(f"Team {i + 1}: {Team.team_scores[i]}")