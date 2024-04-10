# Lab 10.1 Creating a Data Frame
# Author: Fatima Oliveira

import pandas as pd
listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))

csvFilename = 'grades2.csv' # will create a csv file with the dataframe above
df.to_csv(csvFilename)

excelFilename = 'grades.xlsx' # will create a excel file with the dataframe
df.to_excel(excelFilename, index=False, sheet_name='data') # name of the sheet data

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary") # will create another sheet with summary, with the means, as describe() shows.

mean = df.describe().loc['mean','grade'] # will get the mean value in grades
print(mean)
# or same as above
mean = df['grade'].mean() 
print (mean)