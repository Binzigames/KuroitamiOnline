#-------------> importing shit
import pygame as pg
#-------------> load sounds
#>bools
test_sound = None

#>loader
def load_sounds():
    global test_sound
    test_sound = pg.mixer.music.load("sound.mp3")

