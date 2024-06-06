import pygame
import time

class Music:
    def __init__(self) -> None:
        pass

    def playMusic(self, path, duration=None):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        if duration:
            time.sleep(duration)
            pygame.mixer.music.stop()
    
    def stopMusic():
        pygame.mixer.music.stop()

