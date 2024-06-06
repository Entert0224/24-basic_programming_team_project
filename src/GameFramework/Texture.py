from GameFramework import pygame
from GameFramework import os

#텍스쳐를 관리함
class TextureMNG :
    texture_list = {} #불러온 모든 텍스쳐 리스트(불러온 파일을 또 불러오는 것을 방지)

    #텍스쳐(파일)을 불러온다.
    #path : 파일 경로
    @classmethod
    def TextureLoad(cls, path : str) -> pygame.Surface | None :
        if path in cls.texture_list :
            return cls.texture_list[path]

        if os.path.exists(path) : #파일 존재
            print(f"IMG LOAD : {path}")
            texture = pygame.image.load(path) #불러옴
            cls.texture_list[path] = texture #저장
            return texture
        else :
            print(f"IMG FAIL!!! : {path}")
            return None