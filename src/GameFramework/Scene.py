from abc import ABC, abstractmethod

#Scene의 자식클래스가 일정한 구조를 가질 수 있도록 만든 추상클래스
class Scene(ABC) :
    #Scene시작 할 때 한 번만 호출 시키게 만들 추상메서드
    @abstractmethod
    def Setup(self): pass

    #Scene시작 후 계속해서 호출할 (Update)추상메서드
    @abstractmethod
    def Update(self): pass

    #Scene이 다른 Scene으 변경될 때 한 번 호출 되는 추상메서드
    @abstractmethod
    def Exit(self): pass