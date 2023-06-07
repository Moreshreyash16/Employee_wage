'''
@Author: Shreyash More

@Date: 2023-06-04 21:46:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 21:46:30

@Title : Calcilate Employee wage
'''
import random
def employee_attedance():
    """
    Description:
        It calculates the attedance of employee
    Parameter:
        does not take any parameter
    Return:
        Returns if the Employee is present or absent
    """
    attedance=random.randint(0,1)
    if attedance==0:
        return "present"
    else:
        return "absent"

def main():
    print(employee_attedance())

if __name__ == "__main__":
    main()