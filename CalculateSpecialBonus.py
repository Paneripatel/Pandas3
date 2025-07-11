'''
Pandas3

1 Problem 1 :Calculate Special Bonus ( https://leetcode.com/problems/calculate-special-bonus/)

'''

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if (x['employee_id']%2==1) and (x['name'][0]!='M') else 0,axis=1)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')