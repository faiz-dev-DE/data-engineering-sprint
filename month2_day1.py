import pandas as pd

# 1. Fill the missing numerical values to create a valid table
log_data = {
    "emp_id":[101,102,103,104],
    "name": ["Rohan", "Jessica", "Aisha", "Vikram"],
    "salary":[65000,80000,75000,60000],
    "department": ["Data Eng", "Data Eng", "Analytics", "Management"]
           }

# Transform into an indexed Pandas DataFrame
df = pd.DataFrame(log_data)

# 📝 YOUR TASK: Write the missing Pandas commands below:

# Task 1: Print the total rows and columns shape layout 
print(df.shape)


# Task 2: Print only rows where the salary column is strictly greater than 70000
print (df[df["salary"]>70000])

sorted_df= df.sort_values(by="salary" , ascending=False)# df.sort_values does not change any value in the original table untill you explicitly save the result of it in new variable eg:[top_2]
top_2 = sorted_df.iloc[0:2]
print(top_2)


total_salary_by_dept= df.groupby("department")["salary"].sum()
dept_wise_salary= total_salary_by_dept
print(dept_wise_salary)

