# Indexing, Selecting & Assigning
import pandas as pd
mydata = {
    'Cities':['Ujjain','Indore','Bhopal','Gwalior'],
    'Colleges':['MITS','IIT','TIT','ITM'],
}
myvar = pd.DataFrame(mydata)
print(myvar)

x = myvar.Cities # to print the Cities column
print(x)

print(myvar['Colleges']) # more recommended than the dot notation

print(myvar['Colleges'][0]) # to print the specific value in the Colleges column

print(myvar.loc[0]) # to print the first row of the DataFrame

print(myvar.loc[0,'Cities']) # to print the value in the 'Cities' column of the first row

print(myvar.iloc[0,1]) # to print the value in the second column of the first row