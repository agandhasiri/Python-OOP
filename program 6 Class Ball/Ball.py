from math import *

class Ball:
    def __init__(self, px, py, vx, vy):                       # constructor
        self._posX = px                                       # x position of ball
        self._posY = py                                       # y positin of ball
        self._velX = vx                                       # velocity for x 
        self._velY = vy                                       # velocity for y
        

    def advance(self,world):                                

        star=world.getStar()                                  # call star
        
        if star:                                              # if star is present

            X = star.getPositionX()                           # get star's x position
            Y = star.getPositionY()                           # get star's y position
            mass = star.getMass()                             # get star's mass
            d = sqrt((X-self._posX)**2 + (Y-self._posY)**2)   # find the distance between the center of the ball and the center of the star.
            magOfForce = mass / (d**2)                        # find the magnitude of force

            d_X = X - self._posX                              # x distance between star and ball
            f_X = magOfForce * d_X / d                        # force for x 
            d_Y = Y - self._posY                              # y distance between star and ball
            f_Y = magOfForce * d_Y / d                        # force for y

            self._velX += f_X                                 # update the velocites
            self._velY += f_Y
            self._posX += self._velX                          # add updated velocites to the positions
            self._posY += self._velY

                    
        else:                                                 # if there is no star present
            self._posX += self._velX                          # update the positions by adding velocites
            self._posY += self._velY
            self._velY += world.getGravity()                  # update the velocity with gravity
        
        return 


    def getPositionX(self):                                   # to get postion x value of ball
        return  self._posX


    def getPositionY(self):                                   # to get postion y value of ball
        return  self._posY


    def getVelocityX(self):                                   # to get velocity x value of ball
        return  self._velX


    def getVelocityY(self):                                   # to get velocity y value of ball
        return  self._velY





