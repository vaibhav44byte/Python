import pandas as pd

# Summary Functions and Mapping
mdata = {
    'Branch':['CSE','IT','ECE','ME'],
    'Students':[120, 100, 80, 60],
}
df = pd.DataFrame(mdata)
print(df['Branch'])

# Summary functions
print(df.Branch.describe()) # it gives the count, unique values, top value and frequency of the top value in the 'Branch' column
print(df.Students.mean())
print(df.Branch.unique())
print(df.Students.value_counts())

# Maps
def branch_code(branch):
    if branch == 'CSE':
        return 'CS'
    elif branch == 'IT':
        return 'IT'
    elif branch == 'ECE':
        return 'EC'
    elif branch == 'ME':
        return 'ME'
    else:
        return 'Unknown'
df['Branch_Code'] = df.Branch.map(branch_code) # creates a new column 'Branch_Code' by applying the branch_code function to each value in the 'Branch' column
print(df)



