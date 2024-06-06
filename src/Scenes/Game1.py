from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time, Sound
from Scenes import Team
import os
from random import shuffle

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#첫번째 미니게임 Scene
#인물퀴즈 미니게임
class Game1(Scene) :
    shuffled_person = {}
    team_number = 1
    timer = 60
    scores = []
    countdown_number = 4
    picture_number = 0
    is_first_game = True

    is_ready = True
    is_countdown = True
    is_end = False

    desc_panal = None
    start_button = None
    ready_panal = None
    start_text = None
    countdown_text = None
    timer_text = None
    quiz_sprite = None
    o_button = None
    x_button = None
    score_text = None
    next_text = None
    next_button = None
    end_panal = None

    #폴더에 있는 인물 사진을 모두 불러온다.
    @classmethod
    def LoadQuizFile(cls) :
        person_path_name = {}
        for filename in os.listdir("assets/images/인물퀴즈/"):
            image_path = os.path.join("assets/images/인물퀴즈/", filename)
            person_name = os.path.splitext(filename)[0]
            person_path_name[image_path] = person_name

        #랜덤으로 섞는다.
        keys = list(person_path_name.keys())
        shuffle(keys)
        cls.shuffled_person = {key: person_path_name[key] for key in keys}

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        #이 게임이 처음 불러와진 경우
        if cls.is_first_game :
            cls.is_first_game = False
            cls.scores = [0 for i in range(0, Team.Get_team_number_count())]
            cls.desc_panal = Sprite("assets/images/Desc_guess_person.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), layer=13)
            cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 175),layer=14,color=pygame.Color(0,0,0,255))
        else :
            cls.desc_panal = Sprite("assets/images/Desc_guess_person.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), layer=13, visible = False)
            cls.start_text = Sprite("assets/images/start_text2.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),layer=14)

        #퀴즈 불러오기
        cls.LoadQuizFile()

        #배경 및 AI 마크
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        
        #준비
        team_number_text = Text(f"{str(cls.team_number)} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),60,layer=12,fontpath="assets/fonts/H2HDRM.TTF")
        cls.ready_panal = Sprite("assets/images/OX.png",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), scale=Vec2(10,10), layer=10)
        cls.start_button = cls.start_text.CreateButton()

        #시작 전 카운트 다운
        cls.countdown_text = Text(f"3",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),90,layer=5,visible=False,fontpath="assets/fonts/H2HDRM.TTF")
        
        #타이머와 퀴즈 사진
        cls.timer_text = Text("60.00",Vec2(SCREEN_WIDTH/2 - 340, SCREEN_HEIGHT/2 - 270), size=45, fontpath="assets/fonts/H2HDRM.TTF") 
        cls.quiz_sprite = Sprite(list(cls.shuffled_person.keys())[cls.picture_number],Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),visible=False)
        
        #ox 버튼
        o_button = Sprite("assets/images/O_btn.png",Vec2(SCREEN_WIDTH/2 - 81,SCREEN_HEIGHT/2 + 251))
        x_button = Sprite("assets/images/X_btn.png",Vec2(SCREEN_WIDTH/2 + 81,SCREEN_HEIGHT/2 + 251))
        cls.o_button = o_button.CreateButton()
        cls.x_button = x_button.CreateButton()

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

    #퀴즈를 보여준다.
    #사진 보여주기
    @classmethod
    def ShowQuiz(cls) :
        cls.quiz_sprite.SetTexture(list(cls.shuffled_person.keys())[cls.picture_number])
        scale = 390/max(cls.quiz_sprite.rect.width, cls.quiz_sprite.rect.height)
        cls.quiz_sprite.scale = Vec2(scale, scale)
    
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
            cls.quiz_sprite.visible = True
            cls.ShowQuiz()
            
    #게임 시작
    @classmethod
    def Start(cls) :
        cls.timer -= Time.GetDeltaTime()
        if cls.timer < 0 : # 타임오버
            cls.timer = 0
            cls.is_end = True
        cls.timer_text.SetString(f"{cls.timer:.2f}")#시간 텍스트 설정

        is_button_click = False
        if cls.o_button(Vec2(1.1,1.1)) :
            if Mouse.isDown() : #O 버튼을 누를시
                Sound.PlaySound("click")
                is_button_click = True
                cls.scores[cls.team_number - 1] += 1 # 점수추가

        elif cls.x_button(Vec2(1.1,1.1)) :
            if Mouse.isDown() : #X 버튼을 누를시
                Sound.PlaySound("click")
                is_button_click = True

        if is_button_click :
            cls.picture_number += 1 # 다음사진으로
            #준비한 모든 사진을 넘겼다면
            if cls.picture_number >= len(cls.shuffled_person.keys()) :
                cls.is_end = True #게임 끝
                return

            cls.ShowQuiz()

    #게임 끝
    @classmethod
    def End(cls) :
        cls.ready_panal.visible = True
        cls.end_panal.visible = True
        cls.score_text.visible = True

        #점수 세팅
        cur_team_score = cls.scores[cls.team_number - 1]
        cls.score_text.SetString(f"점수 : {cur_team_score} / {len(cls.shuffled_person)}")

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
        cls.shuffled_person = {}
        cls.team_number += 1
        cls.timer = 60
        cls.countdown_number = 4
        cls.picture_number = 0

        cls.is_ready = True
        cls.is_countdown = True
        cls.is_end = False
