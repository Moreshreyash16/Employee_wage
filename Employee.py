'''
@Author: Shreyash More

@Date: 2023-06-04 21:46:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 21:46:30

@Title : Calcilate Employee wage
'''
import random

wage_per_hr=20
full_day_hr=8
half_day_hr=4
working_days=20

def Employee_attedance():
    """
    Description:
        It calculates the attedance of employee
    Parameter:
        does not take any parameter
    Return:
        Returns if the Employee is present or absent
    """
    global attedance
    attedance=random.randint(0,2)
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
        Returns if the daily wage till a condition
    """
    working_hrs=0
    current_working_day=0
    current_wages=0
    while(working_hrs<=100):
        attedance=random.randint(0,2)
        if current_working_day>=20:
            break
        else:
            if attedance==0:
                current_wages+=wage_per_hr*full_day_hr
                working_hrs+=8   
            else:
                current_wages+=wage_per_hr*half_day_hr
                working_hrs+=4
            current_working_day+=1
    return (f" The working hours the worker worked is :{ working_hrs} \n The total wage is {current_wages} \n The total days the worker worked is {current_working_day}")
def main():
    # Employee_attedance()     # printing if Emploee is absent or present
    print(calculateWage())        # printing the Emploee Wages
    # print(f"Total wage is {calculateWage()*working_days}" ) # printing total Emploee Wages
if __name__ == "__main__":
    main()