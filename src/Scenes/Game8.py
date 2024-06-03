from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Time
from Scenes import Global


SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class Game8(Scene) :
    timer = 5.0
    click_count = 0
    
    is_ready = True
    is_playing = False
    is_end = False
    
    start_button = None
    timer_text = None
    click_text = None
    result_text = None
    score_texts = []
    

    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        start_text = Sprite("assets/images/start_text.png", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        cls.start_button = start_text.CreateButton()
        cls.timer_text = Text(f"Time: {cls.timer:.2f}", Vec2(SCREEN_WIDTH / 2, 50), 40, fontpath="assets/fonts/H2HDRM.TTF")
        cls.click_text = Text(f"Clicks: {cls.click_count}", Vec2(SCREEN_WIDTH / 2, 100), 40, fontpath="assets/fonts/H2HDRM.TTF")
        cls.result_text = Text("", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100), 60, fontpath="assets/fonts/H2HDRM.TTF", visible=False)

        for i in range(Global.team-number_count):
            text = Text(f"Team {i + 1}: {Global.team_scores[i]}", Vec2(100, 50 + i * 40), 30, fontpath="assets/fonts/H2HDRM.TTF")
            cls.score_texts.append(text)


    def Ready(cls) :
        if cls.start_button(Vec2(1.25, 1.25)) :
            if Mouse.isDown() :
                cls.is_ready = False
                cls.is_playing = True
           
        
    def Play(cls) :
        cls.timer -= Time.GetDeltaTime()
        
        if cls.timer <= 0 :
            cls.timer = 0
            cls.is_playing = False
            cls.is_end = True
        
        if Mouse.isDown() :
            cls.click_count += 1
            while Mouse.isDown():
                pygame.event.pump()
        
        cls.timer_text.SetString(f"Time: {cls.timer:.2f}")
        cls.click_text.SetString(f"Clicks: {cls.click_count}")

    def End(cls) :
        cls.result_text.visible = True
        Global.team_scores[Global.current_team_index] = cls.click_count

        cls.result_text.SetString(f"Team {Global.current_team_index + 1} Å¬¸¯ ¼ö: {cls.click_count}")

        Global.current_team_index += 1
        if Global.current_team_index >= Global.team_number_count:
            Global.current_team_index = 0
            Director.ChangeScene(GameScene)
        else:
            cls.Reset()
            
    def Update(cls) :
        if cls.is_ready :
            cls.Ready()
        elif cls.is_playing :
            cls.Play()
        elif cls.is_end :
            cls.End()


    @classmethod
    def Reset(cls) :
        cls.timer = 5.0
        cls.click_count = 0
        cls.is_ready = True
        cls.is_playing = False
        cls.is_end = False
        cls.result_text.visible = False

    def Update(cls):
        if cls.is_ready:
            cls.Ready()
        elif cls.is_playing:
            cls.Play()
        elif cls.is_end:
            cls.End()
            

    for i, text in enumerate(cls.score_texts):
        text.SetString(f"Team {i + 1}: {Global.team_scores[i]}")

    def Exit(cls):
        cls.Reset()