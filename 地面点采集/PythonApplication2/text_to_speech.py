#coding=gbk

import pyttsx3

# author = "张蒙蒙"
# date = "2019/04/13"

# 文字朗读
#engine = pyttsx3.init()
#engine.say("有行人, 注意!")
#engine.say("障碍物距离10m!")
#engine.runAndWait()

# 文本朗读
f = open("remind.txt", "r")
line = f.readline()
engine = pyttsx3.init()

while line:
    line = f.readline()
    #print(line, end = '')
    #print(line, end = "")
    engine.say(line)

engine.runAndWait()
f.close()