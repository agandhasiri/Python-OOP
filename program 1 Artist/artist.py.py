from cs1graphics import *
from time import *
#######################################################################################
######################################################################################        #  1
paper = Canvas(1200, 650, 'white', "Friends")


sky = Rectangle(1200, 325, Point(600, 162.5))                         # Sky
sky.setFillColor("skyblue")
sky.setDepth(100)
paper.add(sky)

grass = Rectangle(1200, 325, Point(600, 487.5))                      # Grass
grass.setFillColor((0,250,0))
paper.add(grass)

tree = Layer()                                                       # Tree1

treeTrunk = Rectangle(30, 150, Point(0, 0))
treeTrunk.setFillColor("brown")
treeTrunk.setBorderColor('transparent')
tree.add(treeTrunk)

treePlume = Circle(70, Point(0, -75))
treePlume.setFillColor("green")
treePlume.setDepth(60)
tree.add(treePlume)

paper.add(tree)
tree.move(1050, 300)

tree2 = tree.clone()                                                  # Tree2
paper.add(tree2)
tree2.move(-900, 0)

racetrack = Rectangle(1200, 160, Point(600, 535))                     # race track
racetrack.setFillColor('darkgrey')
paper.add(racetrack)
divider = Path(Point(250, 530), Point(1200, 530))
divider.setBorderWidth(3)
paper.add(divider)
divider2 = Path(Point(250, 450), Point(250, 625))
divider2.setBorderWidth(7)
paper.add(divider2)

##################################################################################
sleep(1)
##################################################################################         #  2

bird = Layer()                                                         # blue bird


Body1 = Circle(60, Point(0, 0))
Body1.setFillColor("blue")

Body2 = Circle(60, Point(-55, -45))
Body2.setFillColor('transparent')
Body2.setBorderWidth(0)

Body4 = Circle(28, Point(25, -50))
Body4.setFillColor('skyblue')
Body4.setBorderWidth(0)

Body3 = Circle(25, Point(30, -30))
Body3.setFillColor("blue")
Body3.setBorderWidth(0)
Body3.setDepth(30)

Beak = Polygon(Point(50, -40), Point(65, -30), Point(50, -20))
Beak.setFillColor("yellow")

birdEye = Circle(5, Point(37, -37))
birdEye.setFillColor("black")
birdEye.setDepth(25)

Wing1 = Circle(15, Point(0, 20))
Wing1.setFillColor('black')
Wing1.setBorderWidth(1)
Wing1.setDepth(25)

Wing2 = Polygon(Point(0, 5), Point(35, 20), Point(-5, 35))
Wing2.setFillColor('black')
Wing2.setDepth(30)
Wing2.rotate(-30)

Leg1 = Path(Point(20, 55), Point(20, 75), Point(20, 65), Point(30, 75), Point(20, 65), Point(10, 75))
Leg1.setBorderWidth(2)
Leg2 = Path(Point(5, 60), Point(5, 75), Point(5, 65), Point(15, 75), Point(5, 65), Point(-5, 75))
Leg2.setBorderWidth(2)

bird.add(Body1)
bird.add(Body2)
bird.add(Body3)
bird.add(Body4)
bird.add(Beak)
bird.add(birdEye)
bird.add(Wing1)
bird.add(Wing2)
bird.add(Leg1)
bird.add(Leg2)
bird.scale(0.5)

paper.add(bird)
bird.move(-20, -20)

for i in range(1, 30):
    bird.rotate(20)
    bird.move(5.15, 5.25)
    bird.rotate(-20)
    sleep(0.05)
# ###################################################################
# #################################################################
bluebaby1 = bird.clone()
bluebaby1.scale(0.3)
paper.add(bluebaby1)
bluebaby1.move(-140, 0)
bluebaby2 = bird.clone()
bluebaby2.scale(0.3)
paper.add(bluebaby2)
bluebaby2.move(-140, 10)
bluebaby3 = bird.clone()
bluebaby3.scale(0.3)
paper.add(bluebaby3)
bluebaby3.move(-140, 15)

sleep(0.2)
for i in range(1, 20):
    bluebaby1.move(10, 2)
    bluebaby2.move(10, 4.5)
    bluebaby3.move(10, 6)
    sleep(0.05)
#########################################################################################
#########################################################################################
bird2 = Layer()                                                            # red Bird


Body1 = Circle(60, Point(0, 0))
Body1.setFillColor("red")

Body2 = Circle(60, Point(-55, -45))
Body2.setFillColor('skyblue')
Body2.setBorderWidth(0)

birdBody4 = Circle(28, Point(25, -50))
birdBody4.setFillColor('skyblue')
birdBody4.setBorderWidth(0)

Body3 = Circle(25, Point(30, -30))
Body3.setFillColor("red")
Body3.setBorderWidth(0)
Body3.setDepth(30)

Beak = Polygon(Point(50, -40), Point(65, -30), Point(50, -20))
Beak.setFillColor("yellow")

birdEye = Circle(5, Point(37, -37))
birdEye.setFillColor("black")
birdEye.setDepth(25)

Wing1 = Circle(15, Point(0, 20))
Wing1.setFillColor('black')
Wing1.setBorderWidth(1)
Wing1.setDepth(25)

Wing2 = Polygon(Point(0, 5), Point(35, 20), Point(-5, 35))
Wing2.setFillColor('black')
Wing2.setDepth(30)
Wing2.rotate(-30)

Leg1 = Path(Point(20, 55), Point(20, 75), Point(20, 65), Point(30, 75), Point(20, 65), Point(10, 75))
Leg1.setBorderWidth(2)
Leg2 = Path(Point(5, 60), Point(5, 75), Point(5, 65), Point(15, 75), Point(5, 65), Point(-5, 75))
Leg2.setBorderWidth(2)

bird2.add(Body1)
bird2.add(Body2)
bird2.add(Body3)
bird2.add(birdBody4)
bird2.add(Beak)
bird2.add(birdEye)
bird2.add(Wing1)
bird2.add(Wing2)
bird2.add(Leg1)
bird2.add(Leg2)
bird2.scale(0.5)
bird2.flip(180)


paper.add(bird2)
bird2.move(1250, 0)

for n in range(1, 20):
    bird2.move(-10, 6.5)
    sleep(0.1)
######################################################################
######################################################################
redbaby1 = bird2.clone()
redbaby1.scale(0.3)
paper.add(redbaby1)
redbaby1.move(180, 45)
redbaby2 = bird2.clone()
redbaby2.scale(0.3)
paper.add(redbaby2)
redbaby2.move(180, 35)
redbaby3 = bird2.clone()
redbaby3.scale(0.3)
paper.add(redbaby3)
redbaby3.move(180, 45)
redbaby1.setDepth(80)
redbaby2.setDepth(80)
redbaby3.setDepth(80)

for m in range(1, 24):
    redbaby1.move(-10, 0)
    redbaby2.move(-9, 0)
    redbaby3.move(-6, 0)
    sleep(0.05)

# ################################################################################################
sleep(1)
# ################################################################################################  # 3
#
turtle=Layer()                                                                        #Turtle  1
w=100
body=Polygon(Point(0*w,0*w),Point(-2.25*w,0*w),Point(-1.8*w,-2*w),Point(-1.5*w,-2.5*w),Point(-w,-3*w),Point(w,-3*w),Point(1.5*w,-2.5*w),Point(1.8*w,-2*w),Point(2.5*w,0*w),Point(0,0))
body.setFillColor("darkgreen")
turtle.add(body)

neck=Rectangle(0.5*w,2*w,Point(-2.25*w,-1*w))
neck.setFillColor("darkgreen")
neck.setBorderColor("darkgreen")
neck.setDepth(70)
neck.adjustReference(-100,-25)
neck.rotate(-15)
neck.adjustReference(0,0)

head=Circle(50,Point(-243,-225))
head.setBorderColor("darkgreen")
head.setFillColor("darkgreen")

headmouth=Ellipse(90,70,Point(-273,-220))
headmouth.setFillColor("darkgreen")
headmouth.setBorderColor("darkgreen")
headmouth.rotate(-15)

eye=Circle(15,Point(-243,-235))
eye.setFillColor("black")

leg=Ellipse(75,180,Point(-125,0))
leg.setFillColor("darkgreen")
leg.setBorderColor("darkgreen")
leg.setDepth(70)

leg2=leg.clone()
leg2.move(250,0)

path1=Path(Point(-190,-150),Point(-150,-100),Point(0,-75),Point(150,-100),Point(195,-150))
path1.setBorderWidth(5)

path2=Path(Point(-130,-270),Point(-100,-200),Point(0,-170),Point(100,-200),Point(130,-270))
path2.setBorderWidth(5)

path3=Path(Point(-75,0),Point(-100,-150),Point(-50,-300))
path3.setBorderWidth(5)

path4=Path(Point(75,0),Point(100,-150),Point(50,-300))
path4.setBorderWidth(5)

turtle.add(neck)
turtle.add(head)
turtle.add(headmouth)
turtle.add(eye)
turtle.add(leg)
turtle.add(leg2)
turtle.add(path1)
turtle.add(path2)
turtle.add(path3)
turtle.add(path4)

paper.add(turtle)

turtle.scale(0.2)
turtle.move(1250,500)

################################################################################
oldturtle=Layer()                                                                    #Turtle 2
w=100
body=Polygon(Point(0*w,0*w),Point(-2.25*w,0*w),Point(-1.8*w,-2*w),Point(-1.5*w,-2.5*w),Point(-w,-3*w),Point(w,-3*w),Point(1.5*w,-2.5*w),Point(1.8*w,-2*w),Point(2.5*w,0*w),Point(0,0))
body.setFillColor("darkgoldenrod")

neck=Rectangle(0.5*w,2*w,Point(-2.25*w,-1*w))
neck.setFillColor("darkgoldenrod")
neck.setBorderColor("darkgoldenrod")
neck.setDepth(70)
neck.adjustReference(-100,-25)
neck.rotate(-15)
neck.adjustReference(0,0)

head=Circle(50,Point(-243,-225))
head.setBorderColor("darkgoldenrod")
head.setFillColor("darkgoldenrod")

headmouth=Ellipse(90,70,Point(-273,-220))
headmouth.setFillColor("darkgoldenrod")
headmouth.setBorderColor("darkgoldenrod")
headmouth.rotate(-15)

eye=Circle(15,Point(-243,-235))
eye.setFillColor("black")

leg=Ellipse(75,180,Point(-125,0))
leg.setFillColor("goldenrod")
leg.setBorderColor("goldenrod")
leg.setDepth(70)

leg2=leg.clone()
leg2.move(250,0)

path1=Path(Point(-190,-150),Point(-150,-100),Point(0,-75),Point(150,-100),Point(195,-150))
path1.setBorderWidth(5)

path2=Path(Point(-130,-270),Point(-100,-200),Point(0,-170),Point(100,-200),Point(130,-270))
path2.setBorderWidth(5)

path3=Path(Point(-75,0),Point(-100,-150),Point(-50,-300))
path3.setBorderWidth(5)

path4=Path(Point(75,0),Point(100,-150),Point(50,-300))
path4.setBorderWidth(5)

oldturtle.add(body)
oldturtle.add(neck)
oldturtle.add(head)
oldturtle.add(headmouth)
oldturtle.add(eye)
oldturtle.add(leg)
oldturtle.add(leg2)
oldturtle.add(path1)
oldturtle.add(path2)
oldturtle.add(path3)
oldturtle.add(path4)

paper.add(oldturtle)
oldturtle.scale(0.2)
oldturtle.move(1250,595)


turtle3=turtle.clone()                                                                     # turtle 3
turtle3.flip(0)
paper.add(turtle3)
turtle3.scale(0.5)
turtle3.move(-1250,-50)



for t in range(1,6):
    turtle.move(-10,0)
    oldturtle.move(-10,0)
    turtle3.move(20,0)
    sleep(0.2)
################################################################################################
sleep(1)
################################################################################################
text=Layer()                                                                          # first message

textBubble=Ellipse(150,75,Point(0,0))
textBubble.setFillColor("white")
textBubblePoint=Polygon(Point(-40,30),Point(-43,45),Point(-35,36))
textBubblePoint.scale(1.5)
textBubblePoint.setFillColor('white')
text.add(textBubble)
text.add(textBubblePoint)

paper.add(text)
text.move(225,55)

textMessage=Text("Hey look,\n turtles are racing.", 10)
textMessage.move(225,55)
paper.add(textMessage)
sleep(3)
paper.remove(text)
paper.remove(textMessage)

##############################################################################################
text0=text.clone()
text0.scale(0.65)
text0.move(-55,340)
paper.add(text0)
text0.scale(0.8)

textMessage0=Text("start", 15)
textMessage0.move(165,390)
paper.add(textMessage0)
sleep(2)
paper.remove(text0)
paper.remove(textMessage0)
#################################################################################

for q in range(1,30):                                                               # race starts
    turtle.move(-20,0)
    oldturtle.move(-10,0)
    sleep(0.2)

##################################################################################

text2=text.clone()
text2.move(700,425)
paper.add(text2)

textMessage2=Text("you are too fast", 14)
textMessage2.move(930,472.5)
paper.add(textMessage2)
sleep(2)
paper.remove(text2)
paper.remove(textMessage2)

##################################################################################

text3=text2.clone()
text3.move(-300,-100)
paper.add(text3)

textMessage3=Text("        Come,\n      lets win this together.", 10)
textMessage3.move(630,375)
paper.add(textMessage3)
sleep(2)
paper.remove(text3)
paper.remove(textMessage3)

##################################################################################

for r in range(1,30):
    oldturtle.move(-10,0)
    sleep(0.2)

##################################################################################

text4=text2.clone()
text4.move(-300,-100)
paper.add(text4)

textMessage4=Text("Ok! Let's go.", 14)
textMessage4.move(630,375)
paper.add(textMessage4)
sleep(2)
paper.remove(text4)
paper.remove(textMessage4)

##################################################################################

for y in range(1,45):
    turtle.move(-10,0)
    oldturtle.move(-10,0)
    sleep(0.1)                                                                        # race ends

###################################################################################
sleep(1)
###################################################################################      #4
text5=text2.clone()                                                                      # chat
text5.scale(0.65)
text5.move(-700,-355)
paper.add(text5)

textMessage5=Text("Mom! who won.", 10)
textMessage5.move(228,129)
paper.add(textMessage5)
sleep(2)
paper.remove(text5)
paper.remove(textMessage5)

text6=text.clone()
text6.move(0,0)
paper.add(text6)

textMessage6=Text("their friendship", 14)
textMessage6.move(225,55)
paper.add(textMessage6)
sleep(2)
paper.remove(text6)
paper.remove(textMessage6)

text7=text.clone()
text7.move(0,0)
paper.add(text7)

textMessage7=Text("               Friends\n     help each other and\n  watch each other grow", 10)
textMessage7.move(225,55)
paper.add(textMessage7)
sleep(4)
paper.remove(text7)
paper.remove(textMessage7)

text8=text2.clone()
text8.scale(0.65)
text8.move(-700,-355)
paper.add(text8)

textMessage8=Text("we have friends\n          too", 10)
textMessage8.move(228,130)
paper.add(textMessage8)
sleep(2)
paper.remove(text8)
paper.remove(textMessage8)


################################################################################################
sleep(1)
################################################################################################       #5
                                                                        #baby birds move
for b in range(1,50):
     bluebaby1.move(4,3)
     bluebaby2.move(5.9,2)
     bluebaby3.move(7.5,1.15)
     redbaby1.move(-5,2.95)
     redbaby2.move(-7,3.1)
     redbaby3.move(-5,3)
     sleep(0.02)

for c in range(1,29):
    bluebaby1.move(0, -10)
    bluebaby2.move(0, -10)
    bluebaby3.move(0, -10)
    redbaby1.move(0, -10)
    redbaby2.move(0, -10)
    redbaby3.move(0, -10)
    sleep(0.02)

##############################################################################
##############################################################################
                                                                                  #FRIENDS TEXT
w=120

F=Path(Point(3.55*w,62.5),Point(3.00*w,62.5),Point(3.00*w,162.5),Point(3.50*w,162.5),Point(3.00*w,162.5),Point(3.00*w,262.5))
F.setBorderWidth(3)
F.setBorderColor("red")
paper.add(F)

R=Path(Point(3.64*w,262.5),Point(3.64*w,62.5),Point(4.19*w,62.5),Point(4.19*w,62.5),Point(3.64*w,162.5),Point(4.19*w,262.5))
R.setBorderWidth(3)
R.setBorderColor("darkorange")
paper.add(R)

I=Path(Point(4.83*w,62.5),Point(4.28*w,62.5),Point(4.555*w,62.5),Point(4.555*w,262.5),Point(4.28*w,262.5),Point(4.83*w,262.5))
I.setBorderWidth(3)
I.setBorderColor("darkgoldenrod")
paper.add(I)

E=Path(Point(5.47*w,62.5),Point(4.92*w,62.5),Point(4.92*w,162.5),Point(5.47*w,162.5),Point(4.92*w,162.5),Point(4.92*w,262.5),Point(5.47*w,262.5))
E.setBorderWidth(3)
E.setBorderColor("darkgreen")
paper.add(E)

N=Path(Point(6.11*w,62.5),Point(6.11*w,262.5),Point(5.56*w,62.5),Point(5.56*w,262.5))
N.setBorderWidth(3)
N.setBorderColor("blue")
paper.add(N)

D=Path(Point(6.20*w,62.5),Point(6.20*w,262.5),)
D.setBorderWidth(3)
D.setBorderColor("darkblue")
d=Spline(Point(6.20*w,62.5),Point(6.45*w,62.5),Point(6.75*w,162.5),Point(6.45*w,262.5),Point(6.20*w,262.5))
d.setBorderWidth(3)
d.setBorderColor("darkblue")
paper.add(D)
paper.add(d)

S=Spline(Point(7.39*w,62.5),Point(6.84*w,92.5),Point(7.115*w,162.5),Point(7.39*w,212.5),Point(6.84*w,262.5))
S.setBorderWidth(3)
S.setBorderColor("darkviolet")
paper.add(S)


###########################################################################################
sleep(1)
###########################################################################################
                                                                           # turtles move
turtle3.flip(180)
for a in range(1,32):
    turtle.move(-10,0)
    oldturtle.move(-10,0)
    turtle3.move(-11,0)
    sleep(0.1)

###############################################################################################   #
                                                                            #baby birds move
for c in range(1,10):
    bluebaby1.move(0, -10)
    bluebaby2.move(0, -10)
    bluebaby3.move(0, -10)
    redbaby1.move(0, -10)
    redbaby2.move(0, -10)
    redbaby3.move(0, -10)
    sleep(0.02)

####################################################################################################
sleep(0.5)
####################################################################################################  #6
bird.flip(180)                                                                # big birds move
sleep(1)
for x in range(1,20):
    bird.move(-10,-10)
    sleep(0.2)
#####################################################################################################

bird2.flip(180)
sleep(1)
for c in range(1,20):
    bird2.move(10,-10)
    sleep(0.2)

#################################################################################################
##################################         THE END       #######################################

