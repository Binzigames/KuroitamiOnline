import pygame as pg
from enum import Enum

class MusicEnum(Enum):
    MENU = "DATA/Music/PainOfLost.ogg"


class MusicManager:
    def __init__(self):
        pg.mixer.init()
        self.current_track = None

    def play(self, track: MusicEnum, loops=1, volume=0.5):
        if self.current_track != track:
            pg.mixer.music.load(track.value)
            pg.mixer.music.set_volume(volume)
            pg.mixer.music.play(loops)
            self.current_track = track

    def stop(self):
        pg.mixer.music.stop()
        self.current_track = None

    def pause(self):
        pg.mixer.music.pause()

    def resume(self):
        pg.mixer.music.unpause()
