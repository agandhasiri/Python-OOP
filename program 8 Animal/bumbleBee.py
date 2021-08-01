from cs1graphics import *
from time import *



class bumbleBee(Layer):                                                                              # A child class of layer                                                                                     

    """ Creates an instance of an bumbleBee as a layer object. """  

    def __init__(self):                                                                              # Constructor            

        """ The reference point of the layer object is centered between the lower legs. """
        super().__init__()                                                                           # call all methods of layer

        self._body=Ellipse(50,100, Point(0, -50))                                                    # circles and ellipses for body, head, eyes
        self._body.setFillColor("yellow")

        self._head = Circle(20, Point(0, -100))
        self._head.setFillColor("yellow")

        self._leftEye = Ellipse(9,12, Point(-10,-100))
        self._leftEye.setFillColor("white")

        self._rightEye = Ellipse(9, 12, Point(10, -100))
        self._rightEye.setFillColor("white")

        self._leftEyePupil = Ellipse(3, 5, Point(-10, -100))
        self._leftEyePupil.setFillColor("black")

        self._rightEyePupil = Ellipse(3, 5,  Point(10, -100))
        self._rightEyePupil.setFillColor("black")
########################################################################

        self._wing1 =   Ellipse(50,20, Point(40, -80))                                              # draw/create wings using ellipses
        self._wing1.setFillColor("white")
        self._wing1.setDepth(70)

        self._wing2 = Ellipse(40, 20, Point(40, -70))
        self._wing2.setFillColor("white")
        self._wing2.setDepth(100)

        self._wing3 =   Ellipse(50,20, Point(-40, -80))
        self._wing3.setFillColor("white")
        self._wing3.setDepth(70)

        self._wing4 = Ellipse(40, 20, Point(-40, -70))
        self._wing4.setFillColor("white")
        self._wing4.setDepth(100)
        
#########################################################################################

        self._bodyStripe1 = Spline(Point(-25,-60), Point(0,-50), Point(25,-60))                    # draw stripes on the body with splines
        self._bodyStripe1.setBorderWidth(3)

        self._bodyStripe2 = Spline(Point(-25, -40), Point(0, -30), Point(25, -40))
        self._bodyStripe2.setBorderWidth(3)

        self._bodyStripe3 = Spline(Point(-20, -20), Point(0, -10), Point(20, -20))
        self._bodyStripe3.setBorderWidth(3)

#######################################################################################
        
        self._leg1 = Path(Point(20,-60), Point(40, -50), Point(55, -30))                           # draw legs using path
        self._leg1.setBorderWidth(2) 

        self._leg2 = Path(Point(20,-40), Point(40, -30), Point(50, -10))
        self._leg2.setBorderWidth(2)

        self._leg3 = Path(Point(15, -18), Point(35, -10), Point(40, 0))
        self._leg3.setBorderWidth(2)

        self._leg4 = Path(Point(-20,-60), Point(-40, -50), Point(-55, -30))
        self._leg4.setBorderWidth(2)

        self._leg5 = Path(Point(-20,-40), Point(-40, -30), Point(-50, -10))
        self._leg5.setBorderWidth(2)

        self._leg6 = Path(Point(-15, -18), Point(-35, -10), Point(-40, 0))
        self._leg6.setBorderWidth(2)
  ######################################################################################
        
        self._leg1dance = Path(Point(20, -60), Point(40, -50), Point(60, -50))                    # draw another leg for dance for each leg
        self._leg1dance.setBorderWidth(2)

        self._leg3dance = Path(Point(15, -18), Point(35, -10), Point(7, 0))
        self._leg3dance.setBorderWidth(2)

        self._leg4dance = Path(Point(-20, -60), Point(-40, -50), Point(-60, -50))
        self._leg4dance.setBorderWidth(2)

        self._leg6dance = Path(Point(-15, -18), Point(-35, -10), Point(-7, 0))
        self._leg6dance.setBorderWidth(2)

##########################################################################################
        
        self._mouth = Spline(Point(-10, -90), Point(0,-80), Point(10,-90))                         # draw mouth using spline
        self._straightMouth = Spline(Point(-10, -90), Point(0,-90), Point(10,-90))

        self._antenna1 =  Spline(Point(3, -118), Point(4, -130),  Point(20, -150))                 # draw antenna's using spline and circle
        self._antenna2 = Spline(Point(-3, -118), Point(-4, -130), Point(-20, -150))

        self._antenna1Cir = Circle(2, Point(20, -150))
        self._antenna1Cir.setFillColor("black")

        self._antenna2Cir = Circle(2, Point(-20, -150))                                             
        self._antenna2Cir.setFillColor("black")
#####################################################################################################


        self._text = Text()                                                                        # create text, add and move 
        self.add(self._text)
        self._text.moveTo(50, -108)
                                                                         

######################################################################################################

        self.add(self._body)                                                                       # add every required part to the layer
        self.add(self._head)
        self.add(self._leftEye)
        self.add(self._rightEye)
        self.add(self._leftEyePupil)
        self.add(self._rightEyePupil)
        self.add(self._wing1)
        self.add(self._wing2)
        self.add(self._wing3)
        self.add(self._wing4)
        self.add(self._bodyStripe1)
        self.add(self._bodyStripe2)
        self.add(self._bodyStripe3)
        self.add(self._leg1)
        self.add(self._leg2)
        self.add(self._leg3)
        self.add(self._leg4)
        self.add(self._leg5)
        self.add(self._leg6)
        self.add(self._mouth)
        self.add(self._antenna1)
        self.add(self._antenna2)
        self.add(self._antenna1Cir)
        self.add(self._antenna2Cir)


    def flapWings(self, flaps):                                                                       # for flapping the wings

        """ This method flaps the bee's wings. It takes one parameter, an integer specifying
            how many times the bird should flap its wings. Default parameter is set to 10.
            Flaps the wings 5 times when no parameter is given. """

        if not isinstance(flaps, int):                                                                # error checking
            raise TypeError("Argument must be an integer.")


        for i in range(flaps):                                                                        # a loop for flaping
            for j in range(10):
                self._wing1.rotate(3)                                                                 # rotate the wings
                self._wing2.rotate(3)
                self._wing3.rotate(-3)
                self._wing4.rotate(-3)
            for j in range(10):                                 
                self._wing1.rotate(-3)                                                              # bring the wings to its original position
                self._wing2.rotate(-3)
                self._wing3.rotate(3)
                self._wing4.rotate(3)

    def setWingColor(self, color):
        
        """ Sets the bee's wings color. This method takes one parameter.
            The parameter is a string and a valid cs1grapgics color name. """

        self._wing1.setFillColor(color)                                                              # set the wings color
        self._wing2.setFillColor(color)
        self._wing3.setFillColor(color)
        self._wing4.setFillColor(color)


    def setHeadColor(self, color):
        
        """ Sets the bee's head color. This method takes one parameter.
            The parameter must be a string and a valid cs1grapgics color name. """

        self._head.setFillColor(color)                                                               # set the head color

    def setBodyColor(self, color):
        
        """ Sets the bee's head color. This method takes one parameter.
            The parameter must be a string and a valid cs1grapgics color name. """

        self._body.setFillColor(color)                                                               # set the body color

    def setAntennaColor(self, color):

        """ Sets the bee's antenna's color. This method takes one parameter.
            The parameter must be a string and a valid cs1grapgics color name. """

        self._antenna1Cir.setFillColor(color)                                                        # set antenna's color
        self._antenna2Cir.setFillColor(color)

        self._antenna1.setBorderColor(color)
        self._antenna2.setBorderColor(color)


    def straightFace(self):

        """ This method smiley face turns to straight smiley face. """ 
        
        self.remove(self._mouth)                                                                     # remove smiley mouth and replace it with straight mouth
        self.add(self._straightMouth)
        sleep(2)
        self.remove(self._straightMouth)                                                             # remove straight mouth and replace it with smiley mouth
        self.add(self._mouth)


    def speak(self, message, fontSize):

        """
            This method takes two parameters, first one is message which must be a string,
            and the second one is font's size which must be an integer. """
        
        if not isinstance(message, str):                                                            # error checking 
            raise TypeError("Argument must be a string.")
        if not isinstance(fontSize, int):
            raise TypeError("Argument must be a string.")

        self._text.setMessage(message)                                                              # set message 
        self._text.setFontSize(fontSize)                                                            # set font size
        sleep(1)
        self.remove(self._text)                                                                     # remove message
                                                                                                    # this method could be written without remove
                                                                                                    # but for easiness i have included it

    def dance(self, steps):

        """ This method takes one parameter which must be  an integer.
            This method changes bee's legs positions with in a range
            of given integer parameter. """
        
        if not isinstance(steps, int):                                                              # error checking
            raise TypeError("Argument must be an integer")

        for i in range(steps):                                                                      # a loop to repeat the dance step

            self.remove(self._leg1)                                                                 # create a dance step by using legs and dancelegs 
            self.remove(self._leg4)
            self.add(self._leg1dance)                                                               # remove and add accordingly
            self.add(self._leg4dance)

            self.remove(self._leg3)
            self.remove(self._leg6)
            self.add(self._leg3dance)
            self.add(self._leg6dance)

            sleep(0.5)

            self.remove(self._leg1dance)
            self.remove(self._leg4dance)
            self.add(self._leg1)
            self.add(self._leg4)

            self.remove(self._leg3dance)
            self.remove(self._leg6dance)
            self.add(self._leg3)
            self.add(self._leg6)

            sleep(0.5)













if __name__ == '__main__' :

    paper=Canvas(900,900)

    myFatherBee = bumbleBee()
    paper.add(myFatherBee)
    myFatherBee.move(150,600)
    myFatherBee.scale(2)

    myBlueBee =bumbleBee()
    myBlueBee.setBodyColor("blue")
    myBlueBee.setHeadColor("blue")
    myBlueBee.setWingColor("gold")
    paper.add(myBlueBee)
    myBlueBee.move(350, 700)

    myRedBee = bumbleBee()
    myRedBee.setBodyColor("red")
    myRedBee.setHeadColor("red")
    myRedBee.setWingColor("gold")
    paper.add(myRedBee)
    myRedBee.move(550, 700)

    myMotherBee = bumbleBee()
    myMotherBee.setBodyColor("green")
    myMotherBee.setHeadColor("green")
    paper.add(myMotherBee)
    myMotherBee.move(750, 600)
    myMotherBee.scale(1.5)

    for i in range(40):
        myBlueBee.move(4.2, -5)
        myBlueBee.flapWings(1)
        myRedBee.move(-4.2, -5)
        myRedBee.flapWings(1)
    myFatherBee.speak("WELCOME", 8)
    myRedBee.speak("TO", 10)
    myBlueBee.speak("OUR", 10)
    myMotherBee.speak("DANCE SHOW", 6)


    myFatherBee.dance(1)
    myFatherBee.flapWings(1)
    myFatherBee.setAntennaColor("blue")
    myFatherBee.setWingColor("blue")
    myBlueBee.dance(1)
    myBlueBee.flapWings(1)
    myBlueBee.setAntennaColor("red")
    myBlueBee.setWingColor("red")
    myRedBee.dance(1)
    myRedBee.flapWings(1)
    myRedBee.setAntennaColor("green")
    myRedBee.setWingColor("green")
    myMotherBee.dance(1)
    myMotherBee.flapWings(1)
    myMotherBee.setAntennaColor("yellow")
    myMotherBee.setWingColor("yellow")


    myRedBee.dance(3)
    myBlueBee.dance(3)
    myRedBee.flapWings(3)
    myBlueBee.flapWings(3)

    myFatherBee.straightFace()
    myMotherBee.straightFace()
    
    myFatherBee.setHeadColor("red")
    myFatherBee.flapWings(10)

    myMotherBee.setHeadColor("blue")
    myMotherBee.flapWings(10)


