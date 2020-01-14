import websocket
#import time
import keyboard 
from vpython import *
ws = websocket.WebSocket()
ws.connect("ws://192.168.43.120")

thresh = 5

def parse(string):
    return [int (element) for element in string.split()]

def getDirection(distances):
    distanceFront = distances[1]
    distanceRight = distances[2]
    distanceLeft = distances[0]
    if(distanceRight<thresh , distanceFront>thresh):
        print('Aagge badho right mat mudna')
    elif(distanceFront<thresh , distanceRight<thresh):
        print('Aagge aur right mat jaana bas')
    elif(distanceFront<thresh , distanceRight>thresh , distanceLeft>thresh):
        print('bhai aagey mat jana')
    elif(distanceFront<thresh , distanceLeft<thresh):
        print('peeche aur right he jaa sakte hain')
    elif(distanceFront>thresh , distanceLeft<thresh):
        print('left mat mudna bhai')
    else:
        print('maaf karo humko nahi pata')
    
size = vector(15,4,0.5)


botAvatar = arrow(pos=vector(0,0,0),axis=vector(0,0,-5),color=color.blue)

frontWall = box(pos=vector(0,0,-thresh), axis=vector(1,0,0), up=vector(0,1,0), size=size)

rightWall = box(pos=vector(thresh,0,0), axis=vector(0,0,-1), up=vector(0,1,0), size=size)

leftWall = box(pos=vector(-thresh,0,0), axis=vector(0,0,-1), up=vector(0,1,0), size=size)

while 1:
    data = ws.recv()
    distances = parse(string=data)

    if distances[1]<thresh :
        colorF=color.red
    else:
        colorF=color.green

    if distances[2]<thresh :
        colorR=color.red
    else:
        colorR=color.green

    if distances[0]<thresh :
        colorL=color.red
    else:
        colorL=color.green
    
    frontWall.color = colorF
    frontWall.pos = vector(0,0,-distances[1])

    rightWall.color=colorR
    rightWall.pos = vector(distances[2],0,0)

    leftWall.color=colorL
    leftWall.pos = vector(-distances[0],0,0)
    
    print(distances)
    if(keyboard.is_pressed('w')):
        ws.send('W')
    if(keyboard.is_pressed('a')):
        ws.send('A')
    if(keyboard.is_pressed('s')):
        ws.send('S')
    if(keyboard.is_pressed('d')):
        ws.send('D')
ws.close()
