#https://leetcode.com/problems/display-the-first-three-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3]