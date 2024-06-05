from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team
from random import shuffle, sample

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class Game9(Scene) :
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

    @classmethod
    def Setup(cls) :
        cls.select_team_number = 2 if Team.Get_current_team_turn() == 1 else 1 

        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        team_number_text = Text(f"{str(Team.Get_current_team_turn())} 팀",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 240),40,fontpath="assets/fonts/H2HDRM.TTF")
        bouns_game_text = Text("보너스 게임!",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 190), 55, fontpath="assets/fonts/H2HDRM.TTF")

        cls.input_box = Sprite("assets/images/input_box.png", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),visible= False)
        cls.up_sprite = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 180, SCREEN_HEIGHT / 2 + 7 - 20), rotation=180, visible= False, color=pygame.Color(255,255,255,195))
        cls.up_button = cls.up_sprite.CreateButton()
        cls.down_sprite = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 180, SCREEN_HEIGHT / 2 + 42 - 20), visible= False, color=pygame.Color(255,255,255,195))
        cls.down_button = cls.down_sprite.CreateButton()
        cls.team_count_text = Text(str(cls.select_team_number), Vec2(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2),40,visible=False, fontpath="assets/fonts/H2HDRM.TTF")

        description = "이번 게임은 보너스 게임이에요.\n다른 팀의 점수를 150 깎을 수 있어요."
        cls.description_text = Text(description,Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 120), 35, fontpath="assets/fonts/H2HDRM.TTF")
        cls.next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), color=pygame.Color(0,0,0,255))
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 170), visible = False, layer=20, color=pygame.Color(0,0,0,255))
        cls.next_button = cls.next_text.CreateButton()
        cls.back_button = cls.back_text.CreateButton()

    @classmethod
    def Description(cls) :
        if cls.next_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                cls.is_description = False
                cls.description_text.SetString("점수를 깎을 팀 번호를 선택해주세요.")

                cls.input_box.visible = True
                cls.up_sprite.visible = True
                cls.down_sprite.visible = True
                cls.team_count_text.visible = True

    @classmethod
    def Start(cls) :
        if cls.next_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                cls.is_start = False

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
        
            
    @classmethod
    def End(cls) :
        cls.input_box.visible = False
        cls.up_sprite.visible = False
        cls.down_sprite.visible = False
        cls.team_count_text.visible = False
        cls.next_text.visible = False
        cls.back_text.visible = True

        cur_team = Team.Get_current_team_turn()
        select_taam = cls.select_team_number
        cls.description_text.SetString(f"{cls.select_team_number}팀의 점수를 150점 깎았습니다.")
        attacked_score = Team.entire_game_score[select_taam - 1] 
        attacked_score -= 150
        if attacked_score < 0 :
            attacked_score = 0
        Team.entire_game_score[select_taam - 1] = attacked_score

        if cls.back_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                from Scenes import GameScene
                Director.ChangeScene(GameScene)

    @classmethod
    def Update(cls) :
        if cls.is_description :
            cls.Description()

        elif cls.is_start :    
            cls.Start()
        
        elif cls.is_end :
            cls.End()

    @classmethod
    def Exit(cls) :
        pass