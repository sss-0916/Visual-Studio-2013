#coding=gbk

import pyttsx3

# author = "������"
# date = "2019/04/13"

# �����ʶ�
#engine = pyttsx3.init()
#engine.say("������, ע��!")
#engine.say("�ϰ������10m!")
#engine.runAndWait()

# �ı��ʶ�
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