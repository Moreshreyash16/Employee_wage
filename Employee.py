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
half_day_hr=4
attedance=random.randint(0,2)
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
        return attedance
    elif attedance==1:
        print("Present but half day")
        return attedance
    else:
        # print ("absent")
        return attedance
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
    elif attedance==1:
        return Wage_per_hr*half_day_hr
    else:
        print("The employee is absent")
        return 0

def main():
    Employee_attedance()     # printing if Emploee is absent or present
    print(f"wage for Day is {calculateWage()}")        # printing the Emploee Wages

if __name__ == "__main__":
    main()