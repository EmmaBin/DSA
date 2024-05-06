#https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd
# reference https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/
#method 1: Calling DataFrame constructor on list
#method 2: we Create a dictionary of lists and then Pass the dictionary to the pd.DataFrame() constructor. 
#Optionally, we can specify the column names for the DataFrame by passing a list of strings to the columns parameter 
#of the pd.DataFrame() constructor.

#method 3: To create a Pandas DataFrame from lists using zip(). 
#We can also use the zip() function to zip together multiple lists to create a DataFrame with more columns.
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # student_id =[]
    # age=[]
    # for values in student_data:
    #     student_id.append(values[0])
    #     age.append(values[1])
    # dict={"student_id": student_id, "age": age}

    # df = pd.DataFrame(dict)
    # return df



    student_id =[]
    age=[]
    for values in student_data:
        student_id.append(values[0])
        age.append(values[1])

    df = pd.DataFrame(list(zip(student_id, age)), columns=["student_id", "age"])
    return df