************************************************************************************____QUESTION____************************************************************************************

#write a Python program, in a file called robots.py, to solve the following problem: 
 
'''Each robot model for a company is designed and created by a single engineer whose nickname is used as the 
name of their robot; the robot model number is derived using a series of steps. Given the nickname, age (as an 
integer) and years of service (as a float value) of an engineer, generate the model number for the robot 
created by that engineer as follows:  
• extract  the  first  and  the  last  character  from  the  engineer's  nickname  and  convert  the  first  extracted 
character to lower case and the last extracted character to upper case to form a string of three characters 
which includes a # concatenated at the end 
• compute the sum of the years of service and age and multiply that sum by 5, then convert it to an integer 
(by truncation, not rounding) 
• generate the  complete  model number as  a  string  by  joining the  digits  of  the  sum with the  reverse  of the 
digits of the sum and repeating the string thus formed, twice; concatenate this string of digits after the string 
of three characters described above 
 
Your Python code should ask the user for the require information and compute and display the robot's name 
and model number.'''

************************************************************************************____CODE____***************************************************************************************

import math

nickname = input("Enter the Engineer's nickname: ")              # asking for users Nickname using input
age = int(input("Enter the Engineer's age: "))                   # asking for Age using input
service = float(input("Enter Engineer's years of service: "))    # asking for year's of service using input
frst_chrctr = nickname[0]                                        # slicing(extracting) the first character from nickname
last_chrctr = nickname[-1]                                       # slicing(extracting) the last character from nickname
initials = (frst_chrctr.lower() + last_chrctr.upper() + "#")     # converting first & last character into lower & upper case
sum = (service + age)*5                                          # adding and multiplying age & service years for model number
sum_trunc = math.trunc(sum)                                      # converting to integer using truncation
model_number = initials + str(sum_trunc) + str(sum_trunc)        # (generating model number and concatenating it twice + converting the 'sum' into string for concatenation.

print("The Robot " + nickname + " has model number " + model_number)   # printing the final generated model number of robot
