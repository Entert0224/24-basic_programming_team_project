from GameFramework import pygame, Vec2, Node, TextureMNG, Director, Renderer

class Sprite(Node) :
    def __init__(self, path : str, position : Vec2 = Vec2(0, 0),
     pivot : Vec2 = Vec2(0.5, 0.5), rotation : float = 0, layer : int = 0,
      ui : bool = False, color : pygame.Color = pygame.Color(255, 255, 255, 255)) -> None :
        super().__init__()
        self.path = path

        self.position : Vec2 = position
        self.pivot = pivot
        self.rotation = rotation
        self.layer = layer
        self.color = color

        self.texture : pygame.Surface = None

        def SetTexture(self, path) : 
            texture : pygame.Surface = TextureMNG.TextureLoad(path)
            if texture != None :
                self.texture = texture
                img_width = texture.get_width()
                img_height = texture.get_height()
                self.rect = pygame.Rect(0, 0, img_width, img_height)


        def Render(self) :
            if self.visible == False : return None
            if self.texture == None : return None

            width = int(self.texture.get_width() * self.scale.x)
            height = int(self.texture.get_height() * self.scale.y)
            draw_image = pygame.transform.scale(self.texture, (width, height))
            
            self.rect = draw_image.get_rect()
            self.rect.centerx = self.position.x - self.rect.width * self.pivot.x
            self.rect.centery = self.position.y - self.rect.height * self.pivot.y
            Director.screen.blit(draw_image, self.rect.topleft)

        def Delete(self) :
            Renderer.DeleteRender(self)


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

        def pointInRect(self, position : tuple, rect : pygame.Rect) -> bool:
            x = position[0]
            y = position[1]
            if rect.right > x and x > rect.left and y > rect.top and y < rect.bottom :
                return True

            return False

        

    