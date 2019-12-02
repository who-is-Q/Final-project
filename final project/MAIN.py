### Created by Shutong Qi #祁舒桐
  # andrew ID : shutongq
import fight
import intro
import scene1
import start
import scene2
import os
from pygame import mixer
#from playsound import playsound
#playsound('Desktop/final project/jianghu.mp3',False)
#from pygame import mixer

mixer.init()
mixer.music.load("Desktop/final project/jianghu.mp3") # Paste The audio file location 
mixer.music.play() 

start.start()
#while not start.strt:

#  start.start()
intro.intro()
scene1.scene1()
fight.fight()
scene2.scene2()
end.end()