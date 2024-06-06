from GameFramework import pygame

#시간 관리하는 클래스
class Time :
    scale = 1 #시간 속도
    clock = None #시간을 불러올 수 있는 pygame패키지 객체
    frame_time_ms = 0 #frame 시간

    #초 단위 시간 deltaTime(frame과 frame 사이의 시간) 반환
    @classmethod
    def GetDeltaTime(cls) :
        if cls.clock == None : return 0
        frame_time_s = cls.frame_time_ms / 1000.0 * cls.scale  # 초 단위
        return frame_time_s

    #시간 속도 설정
    @classmethod
    def SetTimeSpeed(cls, speed : float) :
        cls.scale = speed