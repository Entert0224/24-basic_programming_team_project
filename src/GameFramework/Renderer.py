#이미지와 텍스트의 Render와 Update를 관리하는 클래스
class Renderer:
    node_list = [] #모든 생성된 노드(이미지,텍스트)
    target_render = [] #render(그리기)하기로 되어있는 노드(이미지,텍스트)

    #render(그리기)할 node추가
    @classmethod
    def AddRender(cls, n):
        if n not in cls.target_render:
            cls.target_render.append(n)

    #모든 노드가 담겨있는 리스트에 node추가
    @classmethod
    def AddNode(cls, n):
        if n not in cls.node_list:
            cls.node_list.append(n)
            #layer에 높을 수록 나중에 그리게 해서 다른 이미지보다 위에 있게 한다.
            cls.node_list.sort(key=lambda node: node.layer)

    #관리하고 있는 모든 노드 제거
    @classmethod
    def ClearNode(cls):
        cls.node_list.clear()
        cls.target_render.clear()

    #render할 노드리스트에서 제거
    @classmethod
    def DeleteRender(cls, n):
        if n in cls.target_render:
            cls.target_render.remove(n)

    @classmethod
    def Render(cls):
        #layer에 높을 수록 나중에 그리게 해서 다른 이미지보다 위에 있게 한다.
        cls.target_render.sort(key=lambda node: node.layer)
        for node in cls.target_render:
            node.Render() #해당 노드의 (Render)추상메서드를 구현한 부분 호출
            node.Update() #해당 노드의 (Update)추상메서드를 구현한 부분 호출