### Created by Shutong Qi #祁舒桐
  # andrew ID : shutongq
import start
import intro
import scene1
import fight1
import fight2
import scene2
import scene3
import scene4
import scene5
import end
import os
import setting
from pygame import mixer

mixer.init()
mixer.music.load("Desktop/final project/jianghu.mp3") # Paste The audio file location 
mixer.music.play() 
while not start.start():
    if setting.setting():        
        mixer.music.play() 
    else:
        mixer.music.stop()
    #start.start()
intro.intro()
scene1.scene1()
fight1.fight()
scene2.scene2()
scene3.scene3()
if fight2.fight2() == 1:
    scene5.scene5()
else:
    scene4.scene4()
end.end()