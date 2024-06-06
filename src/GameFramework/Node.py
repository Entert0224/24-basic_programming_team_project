from GameFramework import Vec2, pygame, Renderer
from abc import ABC, abstractmethod

#이미지와 텍스트의 정보만을 담고있는 클래스
class Node(ABC) :
    def __init__(self) -> None :
        self.position : Vec2 = Vec2(0, 0) #위치
        self.scale : Vec2 = Vec2(1, 1) #크기
        self.collision_scale : Vec2 = Vec2(1, 1) #충동크기
        self.pivot : Vec2 = Vec2(0.5, 0.5) #피벗

        self.rotation : float = 0#회전각도(degree)

        self.visible : bool = True#보일지 안보일지

        self.layer : int = 0#layer : layer 높을 수록 다른 이미지위에 있음

        self.color = pygame.Color(255,255,255,255) #색상
        self.rect = pygame.Rect(0,0,0,0) #이미지나 텍스트가 차지하는 사각형
        Renderer.AddNode(self)#전체 노드리스트에 추가

    #이미지를 객체화 했을 때
    #이미지의 Update(정보 지속 변경)부분을 만들기 위해 만든 추상메소드
    @abstractmethod
    def Update(self) : pass

    #이미지의 Render(그리기)부분을 만들기 위해 만든 추상메소드
    @abstractmethod
    def Render(self) : pass