#from GameFramework import Singleton
from GameFramework import pygame 

class Mouse() :
    n_click = 0
    
    @classmethod
    def GetMousePos(cls) -> tuple[int, int]:
        """마우스 위치를 얻어온다."""
        return pygame.mouse.get_pos()

    @classmethod
    def isDown(cls) -> bool:
        """마우스를 누를 때를 감지한다."""
        if cls.n_click == 1 :
            return True
        
        return False

    @classmethod
    def isHold(cls) -> bool:
        """마우스를 누르고 있을 때를 감지한다."""
        if cls.n_click == 2 :
            return True
        
        return False

    @classmethod
    def isUp(cls) -> bool:
        """마우스를 땔 때를 감지한다."""
        if cls.n_click == 3 :
            return True
        
        return False