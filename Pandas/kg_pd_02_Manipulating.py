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

#myvar.set_index("Colleges", inplace=True)
#print(myvar)

# Conditional statements
is_there = myvar.Cities == "Ujjain" # shows which rows have the value "Ujjain" in the 'Cities' column
print(is_there)


 # Assigning values
#myvar['Cities'] = "Mumbai" # to change all the Cities name 
#print(myvar)
myvar.loc[0,"Cities"] = "Vidisha"
print(myvar)