# Programming Excerise #10
#   This program takes a user specified radius value and draws a blue circle with that radius
#   Draws a red radius line segment, and a green diameter line segment
#   After the circle is drawn there is a user option to "View Measurments" which includes displaying
#       the radius value, diameter, circumference, and area. Or specify a "New Circle" by providing a 
#       new radius value. Or Exit the program.

#HOW TO USE THE PROGRAM
#   1) Import circle_radius and the program will run main() upon import
#   2) Click anywhere in the Programming Excerise 10 window
#   3) Enter in a value for the desired radius and click "Set Radius"
#   4) Click "View Measurments" to view the calculated values for a circle with the set radius
#           Click any where in the Circle Measurement window to close it
#   5) Click "New Circle" to draw a new circle with an updated radius
#   6) Click Exit to exit the program

from graphics import *
from math import pi

def main():
    """Main program creates main window and user interaction buttons"""
    #Window
    win = GraphWin("Programming Excerise 10", 400, 400, False)
    #Instructional Message
    messageCenter = Text(Point(200,10), "Click to Set the Circles Radius")
    messageCenter.draw(win)
    #Center Point
    center = Point(200,200)
    centerPoint = Circle(center,2)
    centerPoint.setFill('black')
    centerPoint.draw(win)

    #USER INPUT
    #Mouse click can be any where in the main window
    win.getMouse()
    #Opens input window and sets radius value
    radius = setRadius()
    #Create circleMeasurement
    measurements = circleMeasurement(radius)
    #draw circle in window
    #drawnCicle is a list of all circle elements (circle, radius, diameter, topPoint, leftPoint, rightPoint)
    drawnCircle = drawCircle(center, radius, win)

    #Clears initial instructional message
    messageCenter.undraw()
    #Creates "View Measurement" button in main window
    measurementButton = Text(Point(200,40), "View Measurements").draw(win)
    measurementRect = Rectangle(Point(120,20),Point(280,60)).draw(win)
    #Creates "Exit" button in main window
    exitButton = Text (Point(100,370), "Exit").draw(win)
    exitRect = Rectangle(Point(40,350), Point(160, 390)).draw(win)
    #Creates "New Circle" button in main windo
    newButton = Text (Point(300,370), "New Circle").draw(win)
    newRect = Rectangle(Point(240,350), Point(360, 390)).draw(win)

    #Waits for and gets mouse click location
    clickLocation = getClickLocation(win)
    #While the retruned mouse click location is not within the Exit button
    #Program will do nothing unless mouse click location within View Measurements or New Circle button
    while clickLocation != "exit":
        if clickLocation == "measurements":
            viewMeasurements(measurements)
            #Waits for and gets mouse click location
            clickLocation = getClickLocation(win)
        elif clickLocation == "new":
            #Opens input window and sets radius value
            radius = setRadius()
            #Create circleMeasurement
            measurements = circleMeasurement(radius)
            #Clears the current cirle
                #drawnCicle is list of current cicle elements
                #Iterate through list and undraw each of the elements
            for i in range(len(drawnCircle)):
                drawnCircle[i].undraw()
            #Draw new cicle with the newly set radius
            drawnCircle = drawCircle(center, radius, win)
            #Waits for and gets mouse click location
            clickLocation = getClickLocation(win)
    
    #Mouse Click location within Exit close main window
    win.close()

class circleMeasurement:
    """Creates a circle measurements"""
    def __init__ (self, r):
        """Initialize cube with specified side length"""
        self.r = r
        self.dia = 2*r
        self.circum = round(2 * pi * r,2)
        self.a = round(pi * r**2, 2)
    def getRadius(self):
        """Returns the Radius"""
        return self.r
    def getDiameter(self):
        """Returns the diameter"""
        return self.dia
    def getCircumference(self):
        """Returns the circumference"""
        return self.circum
    def getArea(self):
        """Returns thea area"""
        return self.a

def setRadius():
    """Function which creates user input window and returns the absolute value of the radius value entered"""
    inputWin = GraphWin("Input Radius", 300, 175)
    Text(Point(130,50), "Enter Radius of Circle: ").draw(inputWin)
    input = Entry(Point(235, 50), 5)
    input.setText("0.0")
    input.draw(inputWin)
    #Set radius to user input value
    setRadiusButton = Text(Point(150,100), "Set Radius").draw(inputWin)
    setRadiusRect = Rectangle(Point(100,80),Point(200,120)).draw(inputWin)
    #Get Mouse location - If within the setRadiusRect close window
    clickPoint = inputWin.getMouse()
    closeWindow = checkClick(clickPoint.getX(), clickPoint.getY())
    while not closeWindow:
        clickPoint = inputWin.getMouse()
        closeWindow = checkClick(clickPoint.getX(), clickPoint.getY())
    inputWin.close()

    return abs(float(input.getText()))

def drawCircle(center, radius, w):
    """Function that draws a cicle of specified radius. Draws a radius and diameter line of the circle.
        Resturns a list of circle elements: circle, radius line, diameter line, topPoint, leftPoint rightPoint"""
    userCircle = Circle(center,radius)
    userCircle.setOutline('blue')
    userCircle.setFill('light gray')
    userCircle.draw(w)
    #Draw Radius 
    topCenter = Point(center.getX(), center.getY()-radius)
    radiusLine = Line(Point(center.getX(),center.getY()), Point(topCenter.getX(),topCenter.getY()))
    radiusLine.setOutline('red')
    radiusLine.draw(w)
    #Draw Diameter
    diameterLine = Line(Point(center.getX()+radius,center.getY()),Point(center.getX()-radius,center.getY()))
    diameterLine.setOutline('green')
    diameterLine.draw(w)
    #Draw Center
    centerPoint = Circle(center,2)
    centerPoint.setFill('black')
    centerPoint.draw(w)
    #Draw Radius Point
    topPoint = Circle(topCenter, 2)
    topPoint.setFill('black')
    topPoint.draw(w)
    #Draw Diameter Points
    leftPoint = Circle(Point(center.getX()-radius,center.getY()),2)
    leftPoint.setFill('black')
    leftPoint.draw(w)
    rightPoint = Circle(Point(center.getX()+radius,center.getY()),2)
    rightPoint.setFill('black')
    rightPoint.draw(w)

    return [userCircle, radiusLine, diameterLine, topPoint, leftPoint, rightPoint]

def checkClick(x, y):
    if x >= 120 and x <= 280 and y >= 80 and y <= 120:
        return True
    else:
        return False

def getClickLocation(w):
    """Function that gets the X Y location of the mouse click. Parameters window object"""
    clickPoint = w.getMouse()
    #Action is a string of the button click or False if click not with in button
    action = actionClick(clickPoint.getX(), clickPoint.getY())
    #Loop to wait for mouse click and checks if its within an aciton button
    while not action:
        clickPoint = w.getMouse()
        action = actionClick(clickPoint.getX(), clickPoint.getY())

    #Resturns string of action button name - used for logic handling in main()
    return action

def actionClick(x, y):
    """Function that checks if X Y of a mouse click is located within an action button. Parametets X Y."""
    #Series of Check if X Y of mouse click in rages of action buttons
    if x >= 120 and x <= 280 and y >= 20 and y <= 60:
        return "measurements"
    elif x >= 40 and x <= 160 and y >= 350 and y <= 390:
        return "exit"
    elif x >= 240 and x <= 360 and y >= 350 and y <= 390:
        return "new"
    else:
        return False

def viewMeasurements(measurements):
    """Function that generates circle measurements window and displays measurement value text"""
    measurementWin = GraphWin("Circle Measurements",250, 200)
    #Gets radius from circleMeasurement Object and draws radius text in red
    radiusText = Text(Point(120,25), "Radius = " + str(measurements.getRadius()))
    radiusText.setTextColor('red')
    radiusText.draw(measurementWin)
    #Gets diameter from circleMeasurement Object and draws diameter text in green
    diameterText = Text(Point(120,50), "Diameter = " + str(measurements.getDiameter()))
    diameterText.setTextColor('green')
    diameterText.draw(measurementWin)
    #Get circumference from circleMeasurment Object and draws circumference text in blue
    circumText = Text(Point(120,75), "Circumference = " + str(measurements.getCircumference()))
    circumText.setTextColor('blue')
    circumText.draw(measurementWin)
    #Get area from circleMeasurement Object and draws area text in gray
    areaText = Text(Point(120,100), "Area = " + str(measurements.getArea()))
    areaText.setTextColor('gray')
    areaText.draw(measurementWin)    
    #Display how to close instructional text
    messageBottom= Text(Point(120,185), "Click to Close")
    messageBottom.draw(measurementWin)
    #Waits for mouse click in window then closes
    measurementWin.getMouse()
    measurementWin.close()

main()