from GameFramework import pygame, Vec2, Director, Renderer, Node

#텍스트(글씨) 관리 함수
class Text(Node) :
    #글씨 생성시 호출하는 함수
    #text : 내용
    #position : 위치
    #size : 글씨 크기
    #layer : sprite, text 그리는 순위
    #visible : 보이게할지 안보이게 할지
    #color : 색상
    #fontpath : 폰트 경로
    def __init__(self, text : str = "", position : Vec2 = Vec2(0, 0),
     size : int = 24, layer : int = 0, visible : bool = True,
     color : pygame.Color = pygame.Color(0, 0, 0, 255), fontpath : str = None) :
        super().__init__()
        self.text = text
        self.position = position
        self.size = size
        self.layer = layer
        self.visible = visible
        self.color = color
        self.fontpath = fontpath

        self.font : pygame.font.Font = pygame.font.Font(fontpath, size)

        Renderer.AddRender(self) #Render 할 리스트에 추가

    #Render 목록에서 제거
    def Delete(self) :
        Renderer.DeleteRender(self)

    #추상클래스 문법상 구현
    def Update(self) :
        pass
    
    #텍스트(글씨)를 직접 그리는 부분
    def Render(self) :
        if not self.visible : return
        if not self.text : return

        #글씨 내용에 \n가 있을 경우도 처리하기 위함
        text = self.text.replace(r"\n",'\n')
        lines = text.split('\n')
        rendered_lines = []
        total_height = 0
        
        #한 줄씩 그린다.
        for line in lines:
            #한 줄 그림
            line_surface = self.font.render(line, True, self.color)

            #한 줄의 가로 세로 길이
            width = int(line_surface.get_width() * self.scale.x)
            height = int(line_surface.get_height() * self.scale.y)

            #크기 각도 조절
            line_surface = pygame.transform.scale(line_surface, (width, height))
            line_surface = pygame.transform.rotate(line_surface, self.rotation)

            rendered_lines.append(line_surface)
            total_height += line_surface.get_height()

        #위치 조정
        y_offset = total_height / 2
        for line_surface in rendered_lines:
            self.rect = line_surface.get_rect()
            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y + y_offset - (total_height / 2)

            y_offset += line_surface.get_height()
            #그리기
            Director.screen.blit(line_surface, self.rect)
    
    #글씨 내용 설정
    def SetString(self, text) :
        self.text = text
