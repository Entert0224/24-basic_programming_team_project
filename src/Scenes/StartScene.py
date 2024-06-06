from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Sound
from Scenes import TeamSettingScene, HowScene

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#시작하면 보이는 화면
class StartScene(Scene) :
    question_mark : Sprite = None
    next_button = None
    how_to_play_button = None

    @classmethod
    def Setup(cls) :
        Sound.StopSound("BGM") #중첩 재생 막기 위한 Stop
        Sound.PlaySound("BGM",True) #배경음악 반복 재생
        #배경 및 AI 마크
        start_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))        
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        
        #다음 화면으로 넘어가기 위한 버튼
        next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))      
        cls.next_button = next_text.CreateButton()

        #'어떻게 플레이 하나요?' 버튼
        how_to_play = Sprite("assets/images/how.png", Vec2(SCREEN_WIDTH/2 + 330, SCREEN_HEIGHT/2 + 260))
        cls.how_to_play_button = how_to_play.CreateButton()

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        #다음으로 넘어가기 버튼
        if cls.next_button(Vec2(1.25,1.25)) :
            cls.question_mark.visible = True
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Director.ChangeScene(TeamSettingScene)
        else :
            cls.question_mark.visible = False
        
        #'어떻게 플레이 하나요?' 버튼
        if cls.how_to_play_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Director.ChangeScene(HowScene)

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        pass

