from GameFramework import pygame, Vec2, Node, TextureMNG, Director, Renderer, Mouse

class Sprite(Node) :

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
        self.SetTexture(path)

    def Delete(self) :
        Renderer.DeleteRender(self)

    def Update(self) :
            pass

    def Render(self) :
        if self.visible == False : return None
        if self.texture == None : return None

        width = int(self.texture.get_width() * self.scale.x)
        height = int(self.texture.get_height() * self.scale.y)
        draw_image = pygame.transform.scale(self.texture, (width, height))
        draw_image = pygame.transform.rotate(draw_image, self.rotation)

        draw_image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)

        self.rect = draw_image.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
        Director.screen.blit(draw_image, self.rect)

    def SetTexture(self, path) : 
            texture : pygame.Surface = TextureMNG.TextureLoad(path)
            if texture != None :
                self.texture = texture
                img_width = texture.get_width()
                img_height = texture.get_height()
                self.rect = pygame.Rect(0, 0, img_width, img_height)
                Renderer.AddRender(self)

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

    def GetDistance(self, target : Vec2) :
        pass

    def GetAngle(self, target : Vec2) :
        pass

    def RotationMove(self, speed : float) :
        pass

    def Animation(self, path, frame, tickspeed) :
        pass

    def PointInRect(self, position : tuple) -> bool:
        x = position[0]
        y = position[1]
        if self.rect.right > x and x > self.rect.left and y > self.rect.top and y < self.rect.bottom :
            return True

        return False

    def CreateButton(self):
        set_origin = False
        origin_scale = self.scale
        origin_rotation = self.rotation
        origin_color = self.color

        def Button(scale_effect=Vec2(1, 1), rotation_effect=0, color_effect=pygame.Color(255, 255, 255, 255)) -> bool:
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
        

    