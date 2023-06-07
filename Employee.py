'''
@Author: Shreyash More

@Date: 2023-06-04 21:46:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 21:46:30

@Title : Calcilate Employee wage
'''
import random

Wage_per_hr=20
full_day_hr=8
attedance=random.randint(0,1)
def Employee_attedance():
    """
    Description:
        It calculates the attedance of employee
    Parameter:
        does not take any parameter
    Return:
        Returns if the Employee is present or absent
    """
    
    if attedance==0:
        print("Present")
        return True
    else:
        print ("absent")
        return False
def calculateWage():
    """
    Description:
        It calculates the daily wage of employee
    Parameter:
        does not take any parameter
    Return:
        Returns if the daily wage of employee
    """
    if attedance==0:
        return Wage_per_hr*full_day_hr
    else:
        print("The employee is absent")
        return 0

def main():
    Employee_attedance()     # printing if Emploee is absent or present
    print(calculateWage())        # printing the Emploee Wages


if __name__ == "__main__":
    main()