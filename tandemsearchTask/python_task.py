#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
def get_employees_df():

  return pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
        "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
  )
def get_departments_df():
  dep_df = pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
        "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv"
  )
  dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})

  return dep_df

employees = get_employees_df()
departments = get_departments_df()


# In[19]:


print(employees)


# In[20]:


print(departments)


# In[18]:
#1

print("Please calculate the average, median, lower and upper quartiles of an employees' salaries :")
print("average",employees['SALARY'].mean(),"|","median",employees['SALARY'].median(),"|","lower_quartile",employees['SALARY'].quantile(0.25),"|","upper_quartile",employees['SALARY'].quantile(0.75))



# In[39]:

#2
avg_salary_per_department = employees.groupby('DEPARTMENT_ID')['SALARY'].mean().reset_index()
print("Average Salary per Department:\n", avg_salary_per_department)


# In[43]:

#3
import numpy as np
average_salary = employees['SALARY'].mean()
conditions = [
    (employees['SALARY'] < average_salary),
    (employees['SALARY'] >= average_salary)
]
results = ['low', 'high']
employees['SALARY_CATEGORY'] = np.select(conditions, results)
print(employees)


# In[48]:

#4
import numpy as np
avg_salary_per_department = employees.groupby('DEPARTMENT_ID')['SALARY'].mean().reset_index()
conditions = [
    (employees['SALARY'] < avg_salary_per_department),
    (employees['SALARY'] >= avg_salary_per_department)
]
results = ['low', 'high']
employees['DEPARTMENT_AVG_SALARY'] = np.select(conditions, results)
print(employees)


# In[52]:

#5
employees_dept_20 = employees[employees['DEPARTMENT_ID'] == 20]
print(employees_dept_20)


# In[68]:

#6
def increase_salary(row):
    if row['DEPARTMENT_ID'] == 20:
        return row['SALARY'] * 1.10
    return row['SALARY']

employees['SALARY'] = employees.apply(increase_salary, axis=1)
print(employees)


# In[75]:

#7
empty_phone_numbers = employees[employees['PHONE_NUMBER'].isnull()]
print(empty_phone_numbers)

