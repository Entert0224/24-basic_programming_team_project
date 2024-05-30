from GameFramework import pygame, os

class Sound :
    #파일 이름 : pygame Sound instance
    sound_dict : dict[str, pygame.mixer.Sound] = {}
    
    @staticmethod
    def SoundInit() :
        pygame.mixer.init()

    @classmethod
    def PreLoadSound(cls, folder_path : str):
        if not folder_path.endswith('/') :
            folder_path += "/"

        if not os.path.exists(folder_path) :
            print("Sound Fail : Folder path error")
            return None
        
        #sounds 폴더 내에 있는 모든 소리 preload
        for filename in os.listdir(folder_path):
            if filename.endswith('.wav') or filename.endswith('.mp3'):
                sound_path = os.path.join(folder_path, filename)
                sound = pygame.mixer.Sound(sound_path)
                sound_key = os.path.splitext(filename)[0]
                cls.sound_dict[sound_key] = sound

    @classmethod
    def PlaySound(cls, file_name, loop = False, volume = 0.5) :
        if file_name in cls.sound_dict :
            cls.sound_dict[file_name].set_volume(volume)
            kloop = 0 if loop == False else -1  
            cls.sound_dict[file_name].play(loops = kloop)
        else :
            print(f"Sound Play Fail : File name error : '{file_name}'")

    @classmethod
    def StopSound(cls, file_name) :
        if file_name in cls.sound_dict :
            cls.sound_dict[file_name].stop()
        else :
            print(f"Sound Stop Fail : File name error : '{file_name}'")
