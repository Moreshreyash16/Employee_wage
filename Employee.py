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
working_days=20
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
    wage_for_month=0
    for i in range(working_days):
        attedance=random.randint(0,2)
        if attedance==0:
            wage_for_month += Wage_per_hr*full_day_hr
        elif attedance==1:
            wage_for_month += Wage_per_hr*half_day_hr
    return wage_for_month
def main():
    print(f"Total wage for month is {calculateWage()}" ) # printing total Emploee Wages
if __name__ == "__main__":
    main()