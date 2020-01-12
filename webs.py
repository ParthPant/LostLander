import websocket
#import time
import keyboard 
ws = websocket.WebSocket()
ws.connect("ws://192.168.43.120")

thresh = 10

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
    

while 1:
    data = ws.recv()
    distances = parse(string=data)
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
