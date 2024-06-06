from GameFramework import Scene, Mouse, Renderer, pygame

#Scene을 관리해주는 클래스
class Director :
    __current_scene : Scene = None
    screen_width = 800
    screen_height = 600
    screen : pygame.Surface = None

    event_list = []

    game_running = True

    #스크린 사이즈 설정
    @classmethod
    def SetScreenSize(cls, width, height) :
        cls.screen_width = width
        cls.screen_height = height

    #Driector 클래스 초기 설정
    @classmethod
    def DirectorInit(cls, window_name) :
        cls.screen = pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption(window_name)

    #스크린 원하는 색으로 색칠하기
    @classmethod
    def ScreenFill(cls, color) :
        cls.screen.fill(color)

    #계속해서 Update로 불러와줘야는 함수
    #Scene의 Update를 호출하기 위해
    #마우스 눌림 설정
    @classmethod
    def DirectorUpdate(cls) :
        cur_scene = cls.__current_scene
        if cur_scene != None :
            cur_scene.Update()
            
        cls.event_list = pygame.event.get()[:]
        if(Mouse.n_click == 1) : Mouse.n_click = 2
        elif(Mouse.n_click == 3) : Mouse.n_click = 0

    #원하는 Scene클래스로 변경해준다.
    @classmethod
    def ChangeScene(cls, scene : Scene) :
        cur_scene = cls.__current_scene

        if cur_scene != None :
            cur_scene.Exit()
            Renderer.ClearNode()

        cls.__current_scene = scene
        cls.__current_scene.Setup()

