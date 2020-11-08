import pygame
pygame.init()
from pygame import sysfont

grey=(118,119,110)
yellow=(183,126,8)
black=(0,0,0)
display=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Car Game")
carimg = pygame.image.load("./Images/carnew.png")
#messege_display1("Score:-")
backgroundleft=pygame.image.load("./Images/left1.png")
backgroundright=pygame.image.load("./Images/right1.png")
car_width=48
import time
import random

def messege_display1(text):
    largetext2=pygame.font.Font("freesansbold.ttf",20)
    textsurf1,textrect1=text_object1(text,largetext2)
    textrect1.center=((50),(20))
    display.blit(textsurf1,textrect1)
    #pygame.display.update()
    #loop()

def background():
    display.blit(backgroundleft,(0,0))
    display.blit (backgroundright,(700,0))
    messege_display1("Score:- 395")

def s(text):
    largetext3=pygame.font.Font("freesansold.ttf",80)
    textsurf2,textrect2=text_object1(text,largetext3)
    display.blit(textsurf2,textrect2)


def policecar(police_startx,police_starty,police):
    if police==0:
        police_come=pygame.image.load("./Images/car002.png")
    if police==1:
        police_come=pygame.image.load("./Images/car003.png")
    if police==2:
        police_come=pygame.image.load("./Images/car004.png")
    if police==3:
        police_come=pygame.image.load("./Images/car001.png")


    display.blit(police_come,(police_startx,police_starty))

def centre1_line(centre_startx,centre_starty,centre1):
    if centre1==0:
        line_come1=pygame.image.load("./Images/centre01.png")
    if centre1==1:
        line_come1=pygame.image.load("./Images/centre01.png")

    display.blit(line_come1,(centre_startx,centre_starty))

def side1_line(side1_startx1,side1_starty,side1):
    if side1==0:
        line_come2=pygame.image.load("./Images/line3.png")
    if side1==1:
        line_come2=pygame.image.load("./Images/line4.png")

    display.blit(line_come2,(side1_startx1,side1_starty))

def side2_line(side1_startx2,side1_starty2,side2):
    if side2==0:
        line_come3=pygame.image.load("./Images/line3.png")
    if side2==1:
        line_come3=pygame.image.load("./Images/line4.png")

    display.blit(line_come3,(side1_startx2,side1_starty2))

def side3_line(side3_startx1,side3_starty,side3):
    if side3==0:
        line_come4=pygame.image.load("./Images/line3.png")
    if side3==1:
        line_come4=pygame.image.load("./Images/line4.png")

    display.blit(line_come4,(side3_startx1,side3_starty))

def side4_line(side4_startx2,side4_starty2,side4):
    if side4==0:
        line_come5=pygame.image.load("./Images/line3.png")
    if side4==1:
        line_come5=pygame.image.load("./Images/line4.png")

    display.blit(line_come5,(side4_startx2,side4_starty2))

def left1_line(left1_startx1,left1_starty,left1):
    if left1==0:
        line_come2=pygame.image.load("./Images/left01.png")
    if left1==1:
        line_come2=pygame.image.load("./Images/left02.png")
    if left1==2:
        line_come2=pygame.image.load("./Images/left03.png")
    if left1==3:
        line_come2=pygame.image.load("./Images/left04.png")

    display.blit(line_come2,(left1_startx1,left1_starty))

def left2_line(left1_startx2,left1_starty2,left2):
    if left2==0:
        line_come3=pygame.image.load("./Images/lb01.png")
    if left2==1:
        line_come3=pygame.image.load("./Images/lb02.png")
    #if left2==2:
        #line_come3=pygame.image.load("left03.png")
    #if left2==3:
        #line_come3=pygame.image.load("left04.png")

    display.blit(line_come3,(left1_startx2,left1_starty2))

def right3_line(right3_startx1,right3_starty,right3):
    if right3==0:
        line_come4=pygame.image.load("./Images/right01.png")
    if right3==1:
        line_come4=pygame.image.load("./Images/right03.png")
    if right3==2:
        line_come4=pygame.image.load("./Images/right03.png")

    display.blit(line_come4,(right3_startx1,right3_starty))

def right4_line(right4_startx2,right4_starty2,right4):
    if right4==0:
        line_come5=pygame.image.load("./Images/rb01.png")
    if right4==1:
        line_come5=pygame.image.load("./Images/rb02.png")
    if right4==2:
        line_come5=pygame.image.load("./Images/rb03.png")
    if right4==3:
        line_come5=pygame.image.load("./Images/rb04.png")

    display.blit(line_come5,(right4_startx2,right4_starty2))

def left3_line(left3_startx1,left3_starty,left3):
    if left3==0:
        line_come2=pygame.image.load("./Images/left01.png")
    if left3==1:
        line_come2=pygame.image.load("./Images/left02.png")
    if left3==2:
        line_come2=pygame.image.load("./Images/left03.png")
    if left3==3:
        line_come2=pygame.image.load("./Images/left04.png")

    display.blit(line_come2,(left3_startx1,left3_starty))

def left4_line(left4_startx2,left4_starty2,left4):
    if left4==0:
        line_come3=pygame.image.load("./Images/lb01.png")
    if left4==1:
        line_come3=pygame.image.load("./Images/lb02.png")
    #if left2==2:
        #line_come3=pygame.image.load("left03.png")
    #if left2==3:
        #line_come3=pygame.image.load("left04.png")

    display.blit(line_come3,(left4_startx2,left4_starty2))

def right5_line(right5_startx1,right5_starty,right5):
    if right5==0:
        line_come4=pygame.image.load("./Images/right01.png")
    if right5==1:
        line_come4=pygame.image.load("./Images/right03.png")
    if right5==2:
        line_come4=pygame.image.load("./Images/right03.png")

    display.blit(line_come4,(right5_startx1,right5_starty))

def right6_line(right6_startx2,right6_starty2,right6):
    if right6==0:
        line_come5=pygame.image.load("./Images/rb01.png")
    if right6==1:
        line_come5=pygame.image.load("./Images/rb02.png")
    if right6==2:
        line_come5=pygame.image.load("./Images/rb03.png")
    if right6==3:
        line_come5=pygame.image.load("./Images/rb04.png")

    display.blit(line_come5,(right6_startx2,right6_starty2))


def crash():
    message_display1("Car Crashed")
    pygame.display.update()
    loop()
    #message_display("Your Score:-")

def carsh():
    message_display1(f"Your Score:- 1028")

def message_display1(text):
    largetext = pygame.font.Font("freesansbold.ttf", 140)
    textsurf, textrect = text_object1(text, largetext)
    textrect.center = ((500), (415))
    display.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    loop()

def text_object1(text,font):
    textsurface1=font.render(text,True,yellow)
    return textsurface1,textsurface1.get_rect()


def message_display(text ):
    largetext=pygame.font.Font("freesansbold.ttf",60)
    textsurf,textrect=text_object(text,largetext)
    textrect.center=((500),(300))
    display.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    loop()

def text_object(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def car(x,y):
    display.blit(carimg,(x,y))

def loop ():
    x=400
    y=540
    s=0
    s_change=0
    x_change=0
    y_change=0
    policecar_speed=60
    centre1_line_speed=45
    side1_speed=45
    side2_speed=45
    side3_speed=45
    side4_speed=45

    left1_speed = 45
    left2_speed = 45
    right3_speed = 45
    right4_speed = 45

    left3_speed = 45
    left4_speed = 45
    right5_speed = 45
    right6_speed = 45

    police=0
    centre1=0
    side1=0
    side2=0
    side3=0
    side4=0
    left1 = 0
    left2 = 0
    right3 = 0
    right4 = 0
    left3 = 0
    left4 = 0
    right5 = 0
    right6 = 0

    centre_startx=415
    centre_starty=-600
    centre_width=40
    centre_height=600

    side1_startx1=273
    side1_startx2=560
    side1_starty2=-300
    side1_starty=-600

    side3_startx1 = 273
    side4_startx2 = 560
    side3_starty = -225
    side4_starty2 = -650

    side1_width=20
    side1_height=150
    side2_height=150

    side3_height=150
    side4_height=150

    left1_startx1 = 80
    left1_startx2 = 0
    left1_starty2 = 0
    left1_starty = 0

    right3_startx1 = 700
    right4_startx2 = 808
    right3_starty = 0
    right4_starty2 = 0

    left1_width = 20
    left1_height = 600
    left2_height = 600

    right3_height = 600
    right4_height = 600

    left3_startx1 = 80
    left3_startx2 = 0
    left3_starty2 = -600
    left3_starty = -600

    right5_startx1 = 700
    right6_startx2 = 808
    right5_starty = -600
    right6_starty2 = -600

    left1_width = 20
    left3_height = 600
    left4_height = 600

    right5_height = 600
    right6_height = 600

    police_startx=random.randrange(130,(700-car_width))
    police_starty=-600
    police_width=48
    police_height=70

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-20
                if event.key==pygame.K_RIGHT:
                    x_change=20
            if event.type==pygame.KEYUP:
                x_change=0
        if police_starty < 0:
            s_change =5

            s += s_change



        x+=x_change


        display.fill(grey)
        background()
        side1_starty-=(side1_speed/5)
        side1_line(side1_startx1,side1_starty,side1)
        side1_starty+=side1_speed

        side1_starty2 -= (side2_speed / 5)
        side2_line(side1_startx2, side1_starty2, side2)
        side1_starty2 += side2_speed

        side3_starty -= (side3_speed / 5)
        side3_line(side3_startx1, side3_starty, side3)
        side3_starty += side3_speed

        side4_starty2 -= (side4_speed / 5)
        side4_line(side4_startx2, side4_starty2, side4)
        side4_starty2 += side4_speed

        left1_starty -= (left1_speed / 5)
        left1_line(left1_startx1, left1_starty, left1)
        left1_starty += left1_speed

        left1_starty2 -= (left2_speed / 5)
        left2_line(left1_startx2, left1_starty2, left2)
        left1_starty2 += left2_speed

        right3_starty -= (right3_speed / 5)
        right3_line(right3_startx1, right3_starty, right3)
        right3_starty += right3_speed

        right4_starty2 -= (right4_speed / 5)
        right4_line(right4_startx2, right4_starty2, right4)
        right4_starty2 += right4_speed

        left3_starty -= (left3_speed / 5)
        left3_line(left3_startx1, left3_starty, left3)
        left3_starty += left3_speed

        left3_starty2 -= (left4_speed / 5)
        left4_line(left3_startx2, left3_starty2, left4)
        left3_starty2 += left4_speed

        right5_starty -= (right5_speed / 5)
        right5_line(right5_startx1, right5_starty, right5)
        right5_starty += right5_speed

        right6_starty2 -= (right6_speed / 5)
        right6_line(right6_startx2, right6_starty2, right6)
        right6_starty2 += right6_speed

        centre_starty-=(centre1_line_speed/5)
        centre1_line(centre_startx,centre_starty,centre1)
        centre_starty+=centre1_line_speed
        police_starty-=(policecar_speed/5)
        policecar(police_startx,police_starty,police)
        police_starty+=policecar_speed

        car(x,y)
        #if x<130 or x>700-car_width:
            #carsh()
        if x<130 or x>700-car_width:
            crash()

        if centre_starty>600:
            centre_starty=0-centre_height
            centre_startx=415

            centre1=random.randrange(0,2)

        if side1_starty>600:
            side1_starty=0-side1_height
            side1_startx1=273

            side1=random.randrange(0,2)

        if side1_starty2 > 600:
            side1_starty2 = 0 - side2_height
            side1_startx2 = 560

            side2 = random.randrange(0,2)


        if side3_starty>600:
            side3_starty=0-side3_height
            side3_startx=273

            side3=random.randrange(0,2)

        if side4_starty2 > 600:
            side4_starty2 = 0 - side4_height
            side4_startx2 = 560

            side4 = random.randrange(0, 2)

        if left1_starty>600:
            left1_starty=0-left1_height
            left1_startx1=80

            left1=random.randrange(0,4)

        if left1_starty2 > 600:
            left1_starty2 = 0 - left2_height
            left1_startx2 = 0

            left2 = random.randrange(0,2)


        if right3_starty>600:
            right3_starty=0-right3_height
            right3_startx=700

            right3=random.randrange(0,3)

        if right4_starty2 > 600:
            right4_starty2 = 0 - right4_height
            right4_startx2 = 808

            right4 = random.randrange(0, 4)

        if left3_starty>600:
            left3_starty=0-left3_height
            left3_startx1=80

            left3=random.randrange(0,4)

        if left3_starty2 > 600:
            left3_starty2 = 0 - left4_height
            left3_startx2 = 0

            left4 = random.randrange(0,2)


        if right5_starty>600:
            right5_starty=0-right5_height
            right5_startx=700

            right5=random.randrange(0,3)

        if right6_starty2 > 600:
            right6_starty2 = 0 - right6_height
            right6_startx2 = 808

            right6 = random.randrange(0, 4)

        if police_starty>600:
            police_starty=0-police_height
            police_startx=random.randrange(130,(1000-300))
            police=random.randrange(0,4)

        if y<police_starty+police_height :

           if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
               crash()



        pygame.display.update()



pygame.display.update()
loop()
pygame.quit()
quit()
