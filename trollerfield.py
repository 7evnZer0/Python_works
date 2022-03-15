************************************************************************************____QUESTION____************************************************************************************

#write a Python program, in a file called trollerfield.py, to solve the following problem: 
'''On Trollplanet the trolls want to construct a TrollerField to play the game of Trollering.  Mr. Trollzart, the 
sports manager, commissions an earthling, Mr. Fields, to build the TrollerField. He gives the following sketch 
of the field to Mr. Fields  
 
where the length and the width of the rectangular portion of the field and the major and minor radii of the 
ellipse (both ellipses are the same size) are given by Mr. Trollzart in trollfeet units. To construct the field, Mr. 
Fields' usual fee includes a basic engaging fee of $100 (Canadian dollars) and $20 (Canadian dollars) for every 
square (Earth) foot of the field to be constructed. Mr. Trollzart is willing to pay Mr. Fields in Trollars. Mr. Fields 
understands that five (Earth) feet equals one trollfoot and 50 Trollars is one Canadian dollar. 
 
Write a Python program to help Mr. Fields to convert the given measurements in trollfeet to (Earth) feet and 
based on the computed area of the field and Mr. Fields' usual fees, to compute and display (see sample output 
below) the cost of the field in Trollars.   
 
Call the file containing your program trollerfield.py. 
 
Note:  In the figure given below, the formula to compute the surface area of an ellipse is given and the two 
radii, a and b, are shown, where a is the major radius and b is the minor radius.  Use the constant pi from the 
math library module to compute the area of an ellipse.''' 
 


************************************************************************************____CODE____***************************************************************************************

import math

length = float(input("Enter length of the Rectangle in trollfeet: "))   # Asking for the Length of Rectangle
width = float(input("Enter width of the Rectangle in trollfeet: "))     # Asking for the width of Rectangle
a = float(input("Enter major radius of the Ellipse in trollfeet: "))    # Asking for the major radius of ellipse
b = float(input("Enter minor radius of the Ellipse in trollfeet: "))    # Asking for the minor radius of ellipse
Area_rectangle = length*5*width*5                                       # calculating Area of Rectangle and converting it into sq feet 1 trollfoot = 5 sq feet
Area_ellipse = (math.pi*a*5*b*5)+(math.pi*a*5*b*5)                      # calculating two ellipse areas and converting into sq feet
Total_Area = (Area_rectangle + Area_ellipse)                            # Final Area of Field with rectangle and two ellipse
money_in_CAD = (Total_Area*20) + 100                                    # counting money in Canadian Dollars
troller = money_in_CAD*50                                               # converting CAD into trollers 1 CAD = 50 trollers 

print("The cost to construct a " + str(round(Total_Area,2)) + " sq ft field is " + str(round(troller,2)) + " Trollers.")
    #printing the final value, converting area and amount in string and rounding up the value after two decimals
  
  
