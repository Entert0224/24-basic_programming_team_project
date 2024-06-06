from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import Team

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

#미니게임 진행이 끝나고 보여주는 결과화면
class MiniGameResult(Scene) :
    score_display_text = None
    back_text = None
    back_button = None

    #추상메서드 구현
    #장면 전환 후 한 번 호출 된다.
    #이 미니게임에 필요한 모든 이미지와 텍스트를 그린다.
    #게임에 필요한 모든것을 여기서 미리 설정한다.
    @classmethod
    def Setup(cls) :
        #배경 및 AI 마크
        background = Sprite("assets/images/game_background.jpg",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        Text("-순위 공개-", Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 250), 50, fontpath="assets/fonts/H2HDRM.TTF")

        #1등, 2등, 3등 점수 알려주는 텍스트
        info = "-참고-\n1등 : 100점\n2등 : 80점\n3등 : 50점"
        Text(info, Vec2(SCREEN_WIDTH/2 - 300,SCREEN_HEIGHT/2-100),30, fontpath="assets/fonts/H2HDRM.TTF")
        
        #점수 모여주는 텍스트
        cls.score_display_text = Text("",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 ), 70, 20, False, fontpath="assets/fonts/H2HDRM.TTF")
        
        #뒤로가기(틱택토 화면으로 되돌아가기) 버튼
        cls.back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 265), layer=20, color=pygame.Color(0,0,0,255))
        cls.back_button = cls.back_text.CreateButton()

        #1팀부터 참여한 팀까지 점수와 순위를 나열함
        display_scores_text_ins = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 230), 33, fontpath="assets/fonts/H2HDRM.TTF")
        display_scores_text = ""
        for idx, score in enumerate(Team.game_score) :
            display_scores_text += f"\n{idx + 1}팀 : {score:03d} --- {Team.game_score_rank[idx]}등"
        display_scores_text_ins.SetString(display_scores_text)

        #결과 반영 설명
        description_text = Text("",Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 127), size=29, fontpath="assets/fonts/H2HDRM.TTF") 
    
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

    #Update 추상메서드 구현
    @classmethod
    def Update(cls) :
        #되돌아가기 버튼
        if cls.back_button(Vec2(1.2,1.2)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                from Scenes import GameScene
                Director.ChangeScene(GameScene)#틱택토 화면으로 되돌아간다.

    #Exit 추상메서드 구현
    @classmethod
    def Exit(cls) :
        pass