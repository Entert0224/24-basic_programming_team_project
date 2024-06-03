from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite
from Scenes import Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9, Team
from random import sample 

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class GameScene(Scene) :
    cell : list[Sprite] = []
    cell_button : list = []
    game_background : Sprite = None
    #game_list : list[Scene] = sample([Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9], 9)
    game_list : list[Scene] = [Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9]

    previous_game_index = 0
    played_game_results = dict()

    @classmethod
    def JudgeWinner(cls) :
        if not Team.is_playing : return

        Team.is_playing = False

        odd_sign = Team.ODD_TEAM_SIGN
        even_sign = Team.EVEN_TEAM_SIGN
        winner_sign = odd_sign if Team.JudgeWinner() == odd_sign else even_sign
        cls.played_game_results[cls.previous_game_index] = winner_sign


    @classmethod
    def Setup(cls) :
        cls.JudgeWinner()

        cls.game_background = Sprite("assets/images/GameScene.jpg", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        for i in range(3) :
            for j in range(3) :
                idx = 3 * i + j 
                x = SCREEN_WIDTH / 2 + (135 * (j - 1))
                y = SCREEN_HEIGHT / 2 + 8 + (135 * (i - 1))

                ksprite = None
                if idx in cls.played_game_results :
                    ksprite = Sprite(f"assets/images/{cls.played_game_results[idx]}.png", Vec2(x, y), color=pygame.Color(255,255,255,255))
                else :
                    ksprite = Sprite("assets/images/OX.png", Vec2(x, y), color=pygame.Color(255,255,255,0))
                    cls.cell_button.append(ksprite.CreateButton())

                cls.cell.append(ksprite)
                

        

    @classmethod
    def Update(cls) :
        for idx, cell_btn in enumerate(cls.cell_button) :
            if idx in cls.played_game_results : continue

            if cell_btn(color_effect = pygame.Color(255,255,255,255)) :
                if Mouse.isDown() :
                    Team.is_playing = True
                    Team.Set_current_team_turn(Team.Get_current_team_turn() + 1)
                    cls.previous_game_index = idx
                    cls.played_game_results[idx] = None
                    Director.ChangeScene(cls.game_list[idx])
                    break

    @classmethod
    def Exit(cls) :
        cls.cell.clear()
        cls.cell_button.clear()
        Team.game_score = [0 for i in range(0, Team.Get_team_number_count())]

