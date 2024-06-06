from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team
from random import shuffle, sample

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#일곱번째 Scene
#보너스 게임 : 다른 팀과 점수 맞바꾸기
class Game7(Scene) :
    select_team_number = 0

    is_description = True
    is_start = True
    is_end = True

    description_text = None
    next_text = None
    back_text = None
    next_button = None
    back_button = None
    input_box = None
    up_sprite = None
    down_sprite = None
    up_button = None
    down_button = None
    team_count_text = None
    
    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        cls.select_team_number = 2 if Team.Get_current_team_turn() == 1 else 1 

        #배경, AI 마크, 팀 숫자, 보너스게임 텍스트
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        team_number_text = Text(f"{str(Team.Get_current_team_turn())} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),40,fontpath="assets/fonts/H2HDRM.TTF")
        bouns_game_text = Text("보너스 게임!",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 190), 55, fontpath="assets/fonts/H2HDRM.TTF")

        #입력 박스
        #위 화살표 및 아래 화살표로 숫자를 설정할 수 있도록 이미지 불러옴
        cls.input_box = Sprite("assets/images/input_box.png", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),visible= False)
        cls.up_sprite = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 180, SCREEN_HEIGHT / 2 + 7 - 20), rotation=180, visible= False, color=pygame.Color(255,255,255,195))
        cls.up_button = cls.up_sprite.CreateButton()
        cls.down_sprite = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 180, SCREEN_HEIGHT / 2 + 42 - 20), visible= False, color=pygame.Color(255,255,255,195))
        cls.down_button = cls.down_sprite.CreateButton()
        cls.team_count_text = Text(str(cls.select_team_number), Vec2(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2),40,visible=False, fontpath="assets/fonts/H2HDRM.TTF")

        #보너스 게임 설명
        description = "이번 게임은 보너스 게임이에요.\n우리 팀의 점수와 다른 팀의 점수를 맞바꿔야 해요."
        cls.description_text = Text(description,Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 120), 35, fontpath="assets/fonts/H2HDRM.TTF")
        
        #다음, 뒤로 버튼
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), color=pygame.Color(0,0,0,255))
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()
        cls.back_button = cls.back_text.CreateButton()

    #처음 들어가면 무슨 보너스 게임인지 설명하는 함수
    @classmethod
    def Description(cls) :
        if cls.next_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() : #다음 버튼을 누를 경우
                Sound.PlaySound("click")

                cls.is_description = False
                cls.description_text.SetString("맞바꿀 팀의 번호를 선택해주세요.")

                cls.input_box.visible = True
                cls.up_sprite.visible = True
                cls.down_sprite.visible = True
                cls.team_count_text.visible = True

    #선택
    @classmethod
    def Start(cls) :
        if cls.next_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() : #다음 버튼을 누를 경우
                Sound.PlaySound("click")
                cls.is_start = False #is_start를 False변경하여 end로 넘어간다.

        #점수를 맞바꿀 팀의 숫자를 번튼을 통해서 선택한다.
        if cls.up_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                select_team_number = cls.select_team_number 
                select_team_number += 1
                exculde_team = Team.Get_current_team_turn()
                team_count = Team.Get_team_number_count()
                select_team_number = max(1, min(select_team_number, team_count))
                if exculde_team == select_team_number :
                    if team_count == exculde_team :
                        select_team_number -= 1
                    else :
                        select_team_number += 1

                cls.select_team_number = select_team_number
                cls.team_count_text.SetString(str(select_team_number))

        if cls.down_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                select_team_number = cls.select_team_number 
                select_team_number -= 1
                exculde_team = Team.Get_current_team_turn()
                team_count = Team.Get_team_number_count()
                select_team_number = max(1, min(select_team_number, team_count))
                if exculde_team == select_team_number :
                    if 1 == exculde_team :
                        select_team_number += 1
                    else :
                        select_team_number -= 1

                cls.select_team_number = select_team_number
                cls.team_count_text.SetString(str(select_team_number))
        
    #마무리
    @classmethod
    def End(cls) :
        cls.input_box.visible = False
        cls.up_sprite.visible = False
        cls.down_sprite.visible = False
        cls.team_count_text.visible = False
        cls.next_text.visible = False
        cls.back_text.visible = True

        #점수 맞바꾸기
        cur_team = Team.Get_current_team_turn()
        select_taam = cls.select_team_number
        cls.description_text.SetString(f"{Team.Get_current_team_turn()}팀과 {cls.select_team_number}팀 점수를 맞바꿨습니다.")
        Team.entire_game_score[cur_team - 1],  Team.entire_game_score[select_taam - 1] = Team.entire_game_score[select_taam - 1], Team.entire_game_score[cur_team - 1]

        #게임으로 돌아가기
        if cls.back_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                from Scenes import GameScene
                Director.ChangeScene(GameScene)

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        if cls.is_description :
            cls.Description()

        elif cls.is_start :    
            cls.Start()
        
        elif cls.is_end :
            cls.End()

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        pass