from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Sound, Text
from Scenes import GameScene, Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#참여 팀 수 설정하는 화면
class TeamSettingScene(Scene) :
    question_mark : Sprite = None

    start_button = None
    up_button = None
    down_button = None

    team_count_text : Text = None
    
    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        #배경 및 AI 마크
        team_setting_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        
        #게임 시작 버튼
        start_text = Sprite("assets/images/start_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))  
        cls.start_button = start_text.CreateButton()

        #사용자 안내 해주는 이미지
        team_number_guide = Sprite("assets/images/team_number_guide.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        
        #위 화살표 및 아래 화살표로 숫자를 설정할 수 있도록 이미지 불러옴
        up_button = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 88, SCREEN_HEIGHT / 2 + 7), rotation=180,color=pygame.Color(255,255,255,195))
        cls.up_button = up_button.CreateButton()
        down_button = Sprite("assets/images/up_down_btn.png",Vec2(SCREEN_WIDTH / 2 + 88, SCREEN_HEIGHT / 2 + 42), color=pygame.Color(255,255,255,195))
        cls.down_button = down_button.CreateButton()

        cls.team_count_text = Text(str(Team.Get_team_number_count()), Vec2(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 + 28),40, fontpath="assets/fonts/H2HDRM.TTF")

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        #게임 시작 버튼
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

        #참여하는 팀 수 설정

        #참여 팀수 늘리기
        if cls.up_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() : 
                Sound.PlaySound("click")
                k_number = Team.Get_team_number_count() + 1
                Team.Set_team_number_count(k_number)
                cls.team_count_text.SetString(str(Team.Get_team_number_count()))

        #참여 팀수 줄이기
        if cls.down_button(Vec2(1.1,1.1), 0, color_effect = pygame.Color(255,255,255,255)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                k_number = Team.Get_team_number_count() - 1
                Team.Set_team_number_count(k_number)
                cls.team_count_text.SetString(str(Team.Get_team_number_count()))

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        pass

