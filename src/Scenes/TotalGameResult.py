from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class TotalGameResult(Scene) :
    score_display_text = None
    end_text = None
    end_button = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        Text("-최종 순위 공개-", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 250), 50, fontpath="assets/fonts/H2HDRM.TTF")
        
        cls.score_display_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 ), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        cls.end_text = Sprite("assets/images/END.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 200), layer=20, color=pygame.Color(0,0,0,255))
        cls.end_button = cls.end_text.CreateButton()

        Team.TotalGamescoreGrading()

        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 154), 35, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = ""
        for idx, score in enumerate(Team.entire_game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:03d} --- {Team.entire_game_score_rank[idx]}등"

        display_scores_text_ins.SetString(display_scores_text) 

    @classmethod
    def Update(cls) :
        if cls.end_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                from main import running
                running = False

    @classmethod
    def Exit(cls) :
        pass