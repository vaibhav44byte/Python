import pandas as pd
# creating data
# Data frame is like a table
x = pd.DataFrame({'Yes':[45,56],'No':[36,75]}) # creating dataframe
print(x)

# another method 
mydata = {
    'Cities':['Ujjain','Indore','Bhopal','Gwalior'],
    'Colleges':['MITS','IIT','TIT','ITM'],
}
myvar = pd.DataFrame(mydata)
print(myvar)

# changing index 
myindex = pd.DataFrame(mydata, index=['Row1', 'Row2', 'Row3', 'Row4'])
print(myindex)

# Series (they are like lists)
myseries = pd.Series([1, 2, 3, 4])
print(myseries)