from GameFramework import pygame 

#마우스 관리해주는 클래스
#마우스 사용할때 사용하는 클래스
class Mouse() :
    n_click = 0
    
    #마우스의 화면상의 위치를 얻어온다.
    @classmethod
    def GetMousePos(cls) -> tuple[int, int]:
        return pygame.mouse.get_pos()

    #마우스를 누를 때를 감지한다.
    @classmethod
    def isDown(cls) -> bool:
        if cls.n_click == 1 :
            return True
        
        return False

    #마우스를 누르고 있을 때를 감지한다.
    @classmethod
    def isHold(cls) -> bool:
        if cls.n_click == 2 :
            return True
        
        return False

    #마우스를 땔 때를 감지한다.
    @classmethod
    def isUp(cls) -> bool:
        if cls.n_click == 3 :
            return True
        
        return False