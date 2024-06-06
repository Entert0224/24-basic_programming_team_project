from GameFramework import pygame, Vec2, Node, TextureMNG, Director, Renderer, Mouse

#이미지 관리하는 클래스
class Sprite(Node) :

    #스프라이트 생성할 떄 호출하는 함수
    #path : 이미지경로
    #position : 이미지 위치
    #pivot : 피벗
    #rotation : 이미지 각도
    #scale : 이미지 크기
    #layer : 이미지 그리기 순번
    #visible : 이미지를 보이게 할지 말지
    #color : 이미지 색상
    def __init__(self, path : str, position : Vec2 = Vec2(0, 0),
        pivot : Vec2 = Vec2(0.5, 0.5), rotation : float = 0, scale : Vec2 = Vec2(1,1),
        layer : int = 0, visible : bool = True,
        color : pygame.Color = pygame.Color(255, 255, 255, 255)) -> None :
        super().__init__()
        self.path = path

        self.position : Vec2 = position
        self.pivot = pivot
        self.rotation = rotation
        self.scale = scale
        self.layer = layer
        self.visible = visible
        self.color = color

        self.texture : pygame.Surface = None
        self.SetTexture(path)#이미지 텍스쳐(그림) 불러와서 입히기

    #이미지 삭제 시 render 리스트에서 삭제
    def Delete(self) :
        Renderer.DeleteRender(self)

    #추상메서드 문법 상 구현
    def Update(self) :
            pass

    #실제 이미지를 그리는 함수
    #Renderer클래스에서 계속 호출 중
    def Render(self) :
        if self.visible == False : return None
        if self.texture == None : return None

        #가로, 세로 설정
        width = int(self.texture.get_width() * self.scale.x)
        height = int(self.texture.get_height() * self.scale.y)

        #크기, 각도 설정
        draw_image = pygame.transform.scale(self.texture, (width, height))
        draw_image = pygame.transform.rotate(draw_image, self.rotation)

        #색상 설정
        draw_image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)

        #좌표 설정
        self.rect = draw_image.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
        #화면애 그리기
        Director.screen.blit(draw_image, self.rect)

    # 이미지 텍스쳐(그림) 불러오고 설정함
    # path : 이미지 경로
    def SetTexture(self, path) : 
            #파일에서 이미지 불러옴
            texture : pygame.Surface = TextureMNG.TextureLoad(path)
            if texture != None :
                self.texture = texture #텍스쳐 설정

                #이미지 가로세로 길이 설정 및 rect설정
                img_width = texture.get_width()
                img_height = texture.get_height()
                self.rect = pygame.Rect(0, 0, img_width, img_height)
                Renderer.AddRender(self)#그려줄 renderlist에 추가

    #이미지 Rect범위 가져옴
    def GetRect(self) :
        r : pygame.Rect = None
        
        pos : Vec2 = self.position
        col_scale : Vec2 = self.collision_scale
        scale : Vec2 = self.scale
        img_width = self.texture.get_size()[0]
        img_height = self.texture.get_size()[1]
        pv : Vec2 = self.pivot

        r.right = pos.x + ((col_scale.x * img_width) * pv.x * scale.x)
        r.left = pos.x - ((col_scale.x * img_width) * (1 - pv.x) * scale.x)
        r.top = pos.y - ((col_scale.y * img_height) * (1 - pv.y) * scale.y)
        r.bottom = pos.y + ((col_scale.y * img_height) * pv.y * scale.y)

        return r

    #어떤 좌표가 이미지안에 있나 확인하는 함수
    #position : 좌표
    def PointInRect(self, position : tuple) -> bool:
        x = position[0]
        y = position[1]
        if self.rect.right > x and x > self.rect.left and y > self.rect.top and y < self.rect.bottom :
            return True

        return False

    #이미지 버튼 생성
    #Button 함수를 반환
    def CreateButton(self):
        set_origin = False
        origin_scale = self.scale
        origin_rotation = self.rotation
        origin_color = self.color

        # 버튼의 기능을 도와주는 함수
        # scale_effect : 버튼위로 마우스가 올라갔을 때 크기 변화
        # rotation_effect : 버튼위로 마우스가 올라갔을 때 각도 변화
        # color_effect : 버튼위로 마우스가 올라갔을 때 색상 변화
        def Button(scale_effect=Vec2(1, 1), rotation_effect = self.rotation, color_effect = self.color) -> bool:
            nonlocal set_origin, origin_scale, origin_rotation, origin_color

            if not set_origin:  
                origin_scale = self.scale
                origin_rotation = self.rotation
                origin_color = self.color
                set_origin = True

            if self.PointInRect(Mouse.GetMousePos()):
                self.scale = origin_scale.elementwise() * scale_effect
                self.rotation = origin_rotation + rotation_effect
                self.color = color_effect
                return True
            else:
                self.scale = origin_scale
                self.rotation = origin_rotation
                self.color = origin_color
                set_origin = False
                return False

        return Button
        

    