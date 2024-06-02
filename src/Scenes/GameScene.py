from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite
from Scenes import Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9
from random import sample 

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class GameScene(Scene) :
    cell : list = []
    game_background : Sprite = None
    #game_list : list[Scene] = sample([Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9], 9)
    game_list : list[Scene] = [Game1, Game2, Game3, Game4, Game5, Game6, Game7, Game8, Game9]

    @classmethod
    def Setup(cls) :
        cls.game_background = Sprite("assets/images/GameScene.jpg", Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        for i in range(-1,2,1) :
            for j in range(-1,2,1) :
                x = SCREEN_WIDTH / 2 + (135 * j)
                y = SCREEN_HEIGHT / 2 + 8 + (135 * i)
                ksprite = Sprite("assets/images/OX.png", Vec2(x, y), color=pygame.Color(255,255,255,0))
                cls.cell.append(ksprite.CreateButton())

    @classmethod
    def Update(cls) :
        for idx, cell in enumerate(cls.cell) :
            if cell(color_effect = pygame.Color(255,255,255,255)) :
                if Mouse.isDown() :
                    Director.ChangeScene(cls.game_list[idx])

    @classmethod
    def Exit(cls) :
        pass
