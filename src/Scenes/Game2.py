from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time
from Scenes import Global
import os
from random import shuffle

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class Game2(Scene) :
    team_number = 1
    timer = 60
    scores = [0 for i in range(0, Global.Get_team_number_count())]
    is_ready = True
    is_countdown = True
    countdown_number = 4

    start_button = None
    ready_panal = None
    start_text = None
    countdown_text = None
    timer_text = None
    quiz_sprite = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),layer=11)
        cls.start_button = cls.start_text.CreateButton()

        cls.countdown_text = Text(f"3",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),60,layer=5,visible=False,fontpath="assets/fonts/H2HDRM.TTF")
        
        cls.timer_text = Text("60.00",Vec2(SCREEN_WIDTH/2 - 340, SCREEN_HEIGHT/2 - 270), size=45, fontpath="assets/fonts/H2HDRM.TTF") 
        cls.quiz_sprite = Sprite(list(cls.shuffled_person.keys())[0],Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50),scale=Vec2(0.8,0.8),visible=False)
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
        cls.timer_text.SetString(f"{cls.timer:.2f}")


    @classmethod
    def Update(cls) :
        if cls.is_ready :
            cls.Ready()
        else :
            if cls.is_countdown :
                cls.CountDown()
            else :
                cls.Start() 

    @classmethod
    def Exit(cls) :
        cls.is_countdown = True
        cls.is_ready = True
