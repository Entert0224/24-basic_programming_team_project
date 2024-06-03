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

        text = self.text.replace(r"\n",'\n')
        lines = text.split('\n')
        rendered_lines = []
        max_width = 0
        total_height = 0

        for line in lines:
            line_surface = self.font.render(line, True, self.color)
            width = int(line_surface.get_width() * self.scale.x)
            height = int(line_surface.get_height() * self.scale.y)
            line_surface = pygame.transform.scale(line_surface, (width, height))
            line_surface = pygame.transform.rotate(line_surface, self.rotation)

            rendered_lines.append(line_surface)
            max_width = max(max_width, line_surface.get_width())
            total_height += line_surface.get_height()

        y_offset = total_height / 2
        for line_surface in rendered_lines:
            self.rect = line_surface.get_rect()
            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y + y_offset - (total_height / 2)

            y_offset += line_surface.get_height()
            Director.screen.blit(line_surface, self.rect)

        # draw_text = self.font.render(self.text, True, self.color)

        # width = int(draw_text.get_width() * self.scale.x)
        # height = int(draw_text.get_height() * self.scale.y)
        # draw_text = pygame.transform.scale(draw_text, (width, height))
        # draw_text = pygame.transform.rotate(draw_text, self.rotation)

        # self.rect = draw_text.get_rect()
        # self.rect.centerx = self.position.x
        # self.rect.centery = self.position.y

        # Director.screen.blit(draw_text, self.rect)

    def SetString(self, text) :
        self.text = text
