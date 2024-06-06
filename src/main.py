from GameFramework import Director, Renderer, Mouse, pygame, Time, Sound
from Scenes import StartScene

SCREEN_WIDTH = 800 #화면 가로 길이
SCREEN_HEIGHT = 600 #화면 세로 길이
SCREEN_COLOR = (255, 255, 255)

#게임 시작 전 
def Setup() :
    pygame.init() #pygame init
    Sound.SoundInit() #Sound init에 있는 pygame.mixer init
    Sound.PreLoadSound("assets/sounds/")#폴더에 있는 모든 사운드 미리 불러오기
    Director.SetScreenSize(SCREEN_WIDTH, SCREEN_HEIGHT)#스크린크기 설정
    Director.DirectorInit("Game Tic-Tac-Toe")#화면 만들기
    Time.clock = pygame.time.Clock()

    #최초 화면 전환 실행 
    Director.ChangeScene(StartScene)

#E
def Event() :
    for event in Director.event_list :
        #마우스 클릭 받을 시
        if event.type == pygame.MOUSEBUTTONDOWN :
            Mouse.n_click = 1
        #마우스 클릭을 땔 시
        elif event.type == pygame.MOUSEBUTTONUP :
            Mouse.n_click = 3

        #화면 닫기를 눌렀을 때
        if event.type == pygame.QUIT:
            Director.game_running = False
            
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         Director.game_running = False
    
#업데이트(정보 업데이트)
def Update() :
    Time.frame_time_ms = Time.clock.tick(60)
    Director.ScreenFill(SCREEN_COLOR)
    Director.DirectorUpdate()

#렌더(그리기)
def Render() :
    Renderer.Render() 
    pygame.display.flip()#화면에 그려 놨던 것들 보여주기

#게임을 종료 할 때
def Exit() :
    Renderer.ClearNode()
    pygame.quit()


#main
if __name__ == "__main__" :
    Setup()

    while Director.game_running :
        Event()
        Update()
        Render()
    
    Exit()

