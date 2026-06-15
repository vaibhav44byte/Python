import pandas as pd

# Grouping and sorting
mdata = {
    'Branch':['CSE','IT','ECE','ME'],
    'Students':[120, 100, 80, 60],
}
df = pd.DataFrame(mdata)
print(df.groupby('Branch').Branch.count())
print(df.groupby('Branch').Students.min())
print(df.groupby(['Branch']).Students.agg([len, min, max, sum]))

# Sorting
print(df.sort_values(by='Students')) # sorts the DataFrame by the 'Students' column in ascending order
print(df.sort_values(by='Students', ascending=False)) # sorts the DataFrame by the 'Students' column in descending order
print(df.sort_index())

print(df.sort_values(by=['Branch', 'Students']))