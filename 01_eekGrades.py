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