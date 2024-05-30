from GameFramework import pygame, Vec2, Director, Renderer, Node

class Text(Node) :
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

        Renderer.AddRender(self)

    def Delete(self) :
        Renderer.DeleteRender(self)

    def Update(self) :
        pass

    def Render(self) :
        if not self.visible : return
        if not self.text : return

        draw_text = self.font.render(self.text, True, self.color)

        width = int(draw_text.get_width() * self.scale.x)
        height = int(draw_text.get_height() * self.scale.y)
        draw_text = pygame.transform.scale(draw_text, (width, height))
        draw_text = pygame.transform.rotate(draw_text, self.rotation)

        self.rect = draw_text.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

        Director.screen.blit(draw_text, self.rect)

    def SetString(self, text) :
        self.text = text
