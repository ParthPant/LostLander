from vpython import * 

dF=15
dR=15
dL=6
thresh = 5

def parse(string):
    return string.split()
    
size=vector(15,4,0.5)
#myBall = sphere(pos=vector(0,0,0),
#        radius=0.5)

#directionX = arrow(pos=vector(0,0,0),
#        axis=vector(5,0,0),color=color.red)

#directionY = arrow(pos=vector(0,0,0),
#        axis=vector(0,5,0),color=color.green)

#directionZ = arrow(pos=vector(0,0,0),
#        axis=vector(0,0,-5),color=color.blue)

while 1:
    if dF<thresh :
        colorF=color.red
    else:
        colorF=color.green

    if dR<thresh :
        colorR=color.red
    else:
        colorR=color.green

    if dL<thresh :
        colorL=color.red
    else:
        colorL=color.green

    botAvatar = arrow(pos=vector(0,0,0),axis=vector(0,0,-5),color=color.blue)

    frontWall = box(pos=vector(0,0,-dR), axis=vector(1,0,0), up=vector(0,1,0), size=size,color=colorF)

    rightWall = box(pos=vector(dR,0,0), axis=vector(0,0,-1), up=vector(0,1,0), size=size,color=colorR)

    leftWall = box(pos=vector(-dL,0,0), axis=vector(0,0,-1), up=vector(0,1,0), size=size,color=colorL)

