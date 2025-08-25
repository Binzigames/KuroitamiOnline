import pygame as pg
from enum import Enum

class MusicEnum(Enum):
    MENU = "DATA/Music/PainOfLost.ogg"

MusicBool = True

class MusicManager:
    def __init__(self):
        pg.mixer.init()
        self.current_track = None
        self.current_track_loop = None
        self.current_track_volume = None

    def play(self, track: MusicEnum, loops=1, volume=0.5):
        global MusicBool
        if self.current_track != track and MusicBool:
            pg.mixer.music.load(track.value)
            pg.mixer.music.set_volume(volume)
            pg.mixer.music.play(loops)
            self.current_track_loop = loops
            self.current_track_volume = volume
            self.current_track = track

    def stop(self):
        pg.mixer.music.stop()

    def pause(self):
        pg.mixer.music.pause()

    def resume(self):
        pg.mixer.music.unpause()

    def update(self):
        self.stop()
        self.play(self.current_track , self.current_track_loop , self.current_track_volume)
