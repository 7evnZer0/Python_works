'''Write a program that translates a given grade at the Geekland University into an eek grade. The given grades 
are as follows:  Alpha, Beta, Gamma, Delta, and Epsilon.  Except for the given grade Epsilon, each given grade 
can possibly be followed by a Pu, Mu or Nu tag which adjusts the eek grade accordingly to higher or lower 
status or leaves the eek grade as the given grade.  The eek grades for Alpha, Beta, Gamma, Delta and Epsilon 
are 111111, 11111, 1111, 111 and 11, respectively. A Mu tag with the eek grade for Alpha, Beta, Gamma and 
Delta decreases the eek value of the grade by the eek value itself and a Pu tag with the eek grade for Alpha, 
Beta, Gamma and Delta increases the eek value of the grade by the eek value itself. For example, an Alpha eek 
grade (111111) with a Mu tag would be adjusted to 000000 eek grade, Alpha eek grade (111111) with a Pu tag 
will be adjusted to 222222 and an Alpha eek grade (111111) with a Nu tag will not be adjusted hence the eek 
grade would remain as 111111.
 
Call the file containing your program eekGrades.py.  Don't forget to use constant variables for known 
amounts.  You may assume the user will never enter a tag for Epsilon Pu or Epsilon Mu.'''
-------------------------------------------------------------------------------CODE----------------------------------------------------------------------------------------------------
Alpha = 111111
Beta = 11111
Gamma = 1111
Delta = 111
Epsilon = 11

grade = input("Enter grade as Alpha, Beta, Gamma, Delta or Epsilon: ")
tag = input("Enter the Mu, Pu or Nu: ")

if grade == "Alpha":
    if tag == "Mu":
        print("The numeric eekValue of", grade + " is 000000")
    elif tag == "Pu":
        print("The numeric eekValue of", grade + " is", Alpha+Alpha)
    elif tag == "Nu":
        print("The numeric eekvalue of", grade + " is", Alpha)
elif grade == "Beta" :
    if tag == "Mu":
        print("The numeric eekValue of", grade + " is 00000")
    elif tag == "Pu":
        print("The numeric eekValue of", grade + " is", Beta+Beta) 
    elif tag == "Nu":
        print("The numeric eekValue of", grade + " is", Beta)
elif grade == "Gamma":  
    if tag == "Mu":
        print("The numeric eekValue of", grade + " is 0000")
    elif tag == "Pu":
        print("The numeric eekValue of", grade + " is", Gamma+Gamma)
    elif tag == "Nu":
        print("The numeric eekValue of", grade + " is", Gamma)
elif grade == "Delta":
    if tag == "Mu": 
        print("The numeric eekValue of", grade + " is 000")
    elif tag == "Pu":
        print("The numeric eekValue of", grade + " is", Delta+Delta)
    elif tag == "Nu":
        print("The numeric eekValue of", grade + " is", Delta)
elif grade == "Epsilon" and tag == "Nu":    
    print("The numeric eekValue of", grade + " is", Epsilon)
