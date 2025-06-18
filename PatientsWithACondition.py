'''
3 Problem 3 : Patients with a Condition ( https://leetcode.com/problems/patients-with-a-condition/)
'''

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients[patients['conditions'].str.contains(r"(^|\s)DIAB1", regex=True)]
    return patients[['patient_id', 'patient_name', 'conditions']]