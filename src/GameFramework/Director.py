#from GameFramework import Singleton
from GameFramework import Scene, Mouse, Renderer, pygame


class Director :
    __current_scene : Scene = None
    screen_width = 800
    screen_height = 600
    screen : pygame.Surface = None

    event_list = []

    game_running = True

    @classmethod
    def SetScreenSize(cls, width, height) :
        cls.screen_width = width
        cls.screen_height = height

    @classmethod
    def DirectorInit(cls, window_name) :
        cls.screen = pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption(window_name)

    @classmethod
    def ScreenFill(cls, color) :
        cls.screen.fill(color)

    @classmethod
    def DirectorUpdate(cls) :
        cur_scene = cls.__current_scene
        if cur_scene != None :
            cur_scene.Update()
            
        cls.event_list = pygame.event.get()[:]
        if(Mouse.n_click == 1) : Mouse.n_click = 2
        elif(Mouse.n_click == 3) : Mouse.n_click = 0

    @classmethod
    def ChangeScene(cls, scene : Scene) :
        cur_scene = cls.__current_scene

        if cur_scene != None :
            cur_scene.Exit()
            Renderer.ClearNode()

        cls.__current_scene = scene
        cls.__current_scene.Setup()

