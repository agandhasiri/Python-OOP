from cs1graphics import *

w=int(input("Enter the grid size: "))                         # grid size

paper=Canvas(15*w,13*w, "burlywood4", "Backgammon")

######################################################################################

x,y=4.00*w,6.50*w

for r in range(2):                                   # creates two rectangles

    rectangle=Rectangle(6.00*w,11.00*w, Point(x,y))
    rectangle.setFillColor("navajowhite")
    paper.add(rectangle)
    x += 7.00*w

######################################################################################

x=w
y=6*w

for i in range(12):                                 # for 12 triangles

    triangle_up=Polygon(Point(x,w),Point(w+x,w),Point(w/2+x,y))       # to draw a triangle 
    triangle_up.setBorderWidth(0.03*w)                                
    paper.add(triangle_up)                                  

    triangle_down=triangle_up.clone()                                 # cloning triangle for down side
    paper.add(triangle_down)                           
    triangle_down.rotate(180)                                        # rotate and move to down side
    triangle_down.move(1.00*w,11.00*w)                               # to corner coordinates


    if i%2==0 :
        triangle_up.setFillColor("tan")                              # sets color besed on even or odd
        triangle_down.setFillColor("darkorange")                       
    else :
        triangle_up.setFillColor("darkorange")
        triangle_down.setFillColor("tan")

    x+=w                                                            # adding a grid size to x everytime
                                                                    #    for repetation 
    if x == 7.00 * w:                                               # To make space in the middle
        x += 1.00 * w                                               # jumps a grid size extra 

########################################################################################

r=0.46*w                 # r= radius, num= number of circles at x coordinates(pt), whiteOnTop for color

for num,pt,whiteOnTop in [(2,1.50*w,True), (5,6.50*w,False), (3,9.50*w,False), (5,13.50*w,True)]:

    y = 1.46 * w
    z = 11.54 * w

    for i in range(num):                                 # num of circles

        for v in [y, z]:                                 # drawing circles at two points simultaneously

            circle = Circle(r, Point(pt, v))
            paper.add(circle)

            y +=  r                                        
            z -=  r

            circle.setFillColor("white") if whiteOnTop == True else circle.setFillColor("black")    #setting colors

        circle.setFillColor("black") if whiteOnTop == True else circle.setFillColor("white")     # to change downside circles colors


##########################################################################################

x=1.50*w

for j,i in zip(range(1,13),range(24,12,-1)):          #creating a zip for two ranges
    numbers_up = Text(str(i), 0.33*w)                    #took two text instances to add them simultaneously
    numbers_up.move(x,0.50*w)
    paper.add(numbers_up)
    numbers_down = Text(str(j), 0.33 * w)
    numbers_down.move(x, 12.50 * w)
    paper.add(numbers_down)


    x += 1.00*w                                      
    if x==7.50*w:                                   # to provide space at the middle
        x+=1.00*w                                   # jumps an extra grid size
       

##########################################################################################

divider=Path(Point(7.50*w,0), Point(7.50*w,13.00*w))
divider.setBorderWidth(0.05*w)                            # divider in the middle
paper.add(divider)

#########################################################################################
