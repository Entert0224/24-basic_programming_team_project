from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Sound, Text
from Scenes import GameScene, Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class TeamSettingScene(Scene) :
    question_mark : Sprite = None

    start_button = None
    up_button = None
    down_button = None

    team_count_text : Text = None

    @classmethod
    def Setup(cls) :
        team_setting_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        start_text = Sprite("assets/images/start_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))  
        cls.start_button = start_text.CreateButton()

        team_number_guide = Sprite("assets/images/team_number_guide.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        up_button = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 88, SCREEN_HEIGHT / 2 + 7), rotation=180,color=pygame.Color(255,255,255,195))
        cls.up_button = up_button.CreateButton()
        down_button = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 88, SCREEN_HEIGHT / 2 + 42), color=pygame.Color(255,255,255,195))
        cls.down_button = down_button.CreateButton()

        cls.team_count_text = Text(str(Team.Get_team_number_count()), Vec2(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 + 28),40, fontpath="assets/fonts/H2HDRM.TTF")

    @classmethod
    def Update(cls) :
        if cls.start_button(Vec2(1.25,1.25)) :
            cls.question_mark.visible = True
            if Mouse.isDown() :
                Team.entire_game_score = [0 for i in range(Team.Get_team_number_count())]
                Team.game_score = [0 for i in range(Team.Get_team_number_count())]
                Sound.PlaySound("click")
                Director.ChangeScene(GameScene)
                return
        else :
            cls.question_mark.visible = False

        if cls.up_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                k_number = Team.Get_team_number_count() + 1
                Team.Set_team_number_count(k_number)
                cls.team_count_text.SetString(str(Team.Get_team_number_count()))

        if cls.down_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                k_number = Team.Get_team_number_count() - 1
                Team.Set_team_number_count(k_number)
                cls.team_count_text.SetString(str(Team.Get_team_number_count()))

    @classmethod
    def Exit(cls) :
        pass

