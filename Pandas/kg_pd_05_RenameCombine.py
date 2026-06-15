import pandas as pd
# Renaming and combining
mdata = {
    'Branch':['CSE','IT','ECE','ME'],
    'Students':[120, 100, 80, 60],
}

df = pd.DataFrame(mdata)
# Renaming columns
df.rename(columns={'Branch':'Department'}, inplace=True)
print(df)