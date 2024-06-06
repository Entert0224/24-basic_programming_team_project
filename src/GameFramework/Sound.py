from GameFramework import pygame, os

#사운드(소리)를 관리하는 클래스
class Sound :
    #파일 이름(key) : pygame Sound instance (value)
    sound_dict : dict[str, pygame.mixer.Sound] = {}
    
    #사운드 믹서 초기화
    @staticmethod
    def SoundInit() :
        pygame.mixer.init()

    #파일에 있는 모든 사운드를 미리 불러와 dictionary 저장해 둔다.
    #folder_path : 폴더 경로
    @classmethod
    def PreLoadSound(cls, folder_path : str):
        #입력한 path가 /로 끝나지 않을 경우
        if not folder_path.endswith('/') : 
            folder_path += "/" # '/' 을 추가한다.

        #사운드가 담겨있는 폴더가 존재하지 않을 경우
        if not os.path.exists(folder_path) : 
            print("Sound Fail : Folder path error")
            return None
        
        #sounds 폴더 내에 있는 모든 소리(.mp3 or .wav) 파일을 모두 미리 불러내고 저장한다.
        for filename in os.listdir(folder_path):
            if filename.endswith('.wav') or filename.endswith('.mp3'):
                sound_path = os.path.join(folder_path, filename)
                sound = pygame.mixer.Sound(sound_path)
                sound_key = os.path.splitext(filename)[0]
                cls.sound_dict[sound_key] = sound

    #소리를 재생 시키고 싶을때 파일 이름만 입력
    #file_name : 파일 이름
    #loop : 이 소리를 반복시킬 건가
    #volume : 소리크기
    @classmethod
    def PlaySound(cls, file_name, loop = False, volume = 0.5) :
        if file_name in cls.sound_dict :
            cls.sound_dict[file_name].set_volume(volume)
            kloop = 0 if loop == False else -1  
            cls.sound_dict[file_name].play(loops = kloop)
        else :
            print(f"Sound Play Fail : File name error : '{file_name}'")

    #재생하고 있는 소리를 멈춘다.
    #file_name : 파일 이름
    @classmethod
    def StopSound(cls, file_name) :
        if file_name in cls.sound_dict :
            cls.sound_dict[file_name].stop()
        else :
            print(f"Sound Stop Fail : File name error : '{file_name}'")
