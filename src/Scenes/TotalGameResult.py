from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#틱택토가 끝나고 보여주는 최종 결과화면
class TotalGameResult(Scene) :
    score_display_text = None
    end_text = None
    end_button = None

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        #배경 및 AI 마크
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        Text("-최종 순위 공개-", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 250), 50, fontpath="assets/fonts/H2HDRM.TTF")
        
        #순위 보여주기
        cls.score_display_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 ), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        cls.end_text = Sprite("assets/images/END.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 210), layer=20, color=pygame.Color(0,0,0,255))
        cls.end_button = cls.end_text.CreateButton()

        #최종 순위 매기기
        Team.TotalGamescoreGrading()

        #1팀부터 참여한 팀까지 점수와 순위를 나열함
        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 185), 32, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = ""
        for idx, score in enumerate(Team.entire_game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:03d} --- {Team.entire_game_score_rank[idx]}등"

        display_scores_text_ins.SetString(display_scores_text) 

    @classmethod
    def Update(cls) :
        #프로그램 끝내기
        if cls.end_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Director.game_running = False

    @classmethod
    def Exit(cls) :
        pass