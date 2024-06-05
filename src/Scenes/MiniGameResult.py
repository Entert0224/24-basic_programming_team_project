from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class MiniGameResult(Scene) :
    score_display_text = None
    back_text = None
    back_button = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        Text("-순위 공개-", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 250), 50, fontpath="assets/fonts/H2HDRM.TTF")
        
        cls.score_display_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 ), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 265), layer=20, color=pygame.Color(0,0,0,255))
        cls.back_button = cls.back_text.CreateButton()

        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 230), 33, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = ""
        for idx, score in enumerate(Team.game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:03d} --- {Team.game_score_rank[idx]}등"

        display_scores_text_ins.SetString(display_scores_text)

        description_text = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 127), size=30, fontpath="assets/fonts/H2HDRM.TTF") 

        winner_judge = [index + 1 for index, value in enumerate(Team.game_score_rank) if value == 1]
        winner_judge_num_text = map(str,winner_judge)
        winner_judge_text = ", ".join(winner_judge_num_text)
        if all(i % 2 == 0 for i in winner_judge):
            description_text.SetString(f"{winner_judge_text}팀이 1등을 했어요.\n이번 미니게임은 짝수 팀이 이겼어요.")
        elif all(i % 2 != 0 for i in winner_judge):
            description_text.SetString(f"{winner_judge_text}팀이 1등을 했어요.\n이번 미니게임은 홀수 팀이 이겼어요.")
        else:
            is_even = "짝" if Team.Get_current_team_turn() % 2 == 0 else "홀"
            description_text.SetString(f"{winner_judge_text}팀이 1등을 했어요.\n이번 미니게임은 우열을 가리기 힘들어요.\n이 게임을 선택한 {Team.Get_current_team_turn()}팀이 {is_even}수 팀이라\n {is_even}수 팀 승!")

    @classmethod
    def Update(cls) :
        if cls.back_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                from Scenes import GameScene
                Director.ChangeScene(GameScene)

    @classmethod
    def Exit(cls) :
        pass