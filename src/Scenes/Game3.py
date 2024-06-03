from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time
from Scenes import Team
from random import randint

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class Game3(Scene) :
    team_number = 1
    scores = [0 for i in range(0, Team.Get_team_number_count())]

    input_text = ""

    is_ready = True
    is_end = False

    start_button = None
    ready_panal = None
    start_text = None
    next_text = None
    back_text = None
    next_button = None
    back_button = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),layer=11)
        cls.start_button = cls.start_text.CreateButton()

        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(255,255,255,255))
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(255,255,255,255))
        cls.next_button = cls.next_text.CreateButton()
        cls.back_button = cls.back_text.CreateButton()

    @classmethod
    def Event(cls) :
        input_text = cls.input_text
        for event in pygame.event.get():
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
                
        cls.input_text = input_text
        
    @classmethod
    def Ready(cls) :
        if cls.start_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                cls.is_ready = False
                cls.ready_panal.visible = False
                cls.start_text.visible = False

    @classmethod
    def Start(cls) :
        if cls.o_button(Vec2(1.1,1.1)) :
            if Mouse.isDown() :
                cls.is_end = True

            
    @classmethod
    def End(cls) :
        cls.ready_panal.visible = True
        cur_team_score = cls.scores[cls.team_number - 1]

        Team.game_score[cls.team_number - 1] = cur_team_score # TODO 점수 매기는 방식

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

        if not cls.is_end :    
            cls.Start()
        else :
            cls.End()

    @classmethod
    def Exit(cls) :
        cls.team_number += 1

        cls.is_ready = True
        cls.is_end = False