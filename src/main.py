from GameFramework import Director, Renderer, Mouse, pygame, Time, Sprite, Sound
from Scenes import StartScene

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (255, 255, 255)

def Setup() :
    pygame.init()
    Sound.SoundInit()
    Sound.PreLoadSound("assets/sounds/")
    Director.SetScreenSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    Director.DirectorInit("Game Tic-Tac-Toe")
    Time.clock = pygame.time.Clock()

    Director.ChangeScene(StartScene)

def Event() :
    for event in Director.event_list :
        if event.type == pygame.MOUSEBUTTONDOWN :
            Mouse.n_click = 1

        elif event.type == pygame.MOUSEBUTTONUP :
            Mouse.n_click = 3

        if event.type == pygame.QUIT:
            Director.game_running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Director.game_running = False
        
def Update() :
    Time.frame_time_ms = Time.clock.tick(60)
    Director.ScreenFill(SCREEN_COLOR)
    Director.DirectorUpdate()

def Render() :
    Renderer.Render()
    pygame.display.flip()

def Exit() :
    Renderer.ClearNode()
    pygame.quit()


if __name__ == "__main__" :
    Setup()

    while Director.game_running :
        Event()
        Update()
        Render()
    
    Exit()

