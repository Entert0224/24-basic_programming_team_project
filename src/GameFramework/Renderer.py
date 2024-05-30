from GameFramework import pygame

class Renderer:
    node_list = []
    target_render = []

    @classmethod
    def AddRender(cls, n):
        if n not in cls.target_render:
            cls.target_render.append(n)

    @classmethod
    def AddNode(cls, n):
        if n not in cls.node_list:
            cls.node_list.append(n)
            cls.node_list.sort(key=lambda node: node.layer)

    @classmethod
    def ClearNode(cls):
        cls.node_list.clear()
        cls.target_render.clear()

    @classmethod
    def DeleteRender(cls, n):
        if n in cls.target_render:
            cls.target_render.remove(n)

    @classmethod
    def Render(cls):
        cls.target_render.sort(key=lambda node: node.layer)
        for node in cls.target_render:
            node.Render()
            node.Update()