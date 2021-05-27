import csv
with open('class2.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)  

totalMarks= 0
totalEnteries= len(fileData)

for marks in fileData:
    totalMarks += float(marks[1])
    mean= totalMarks/totalEnteries

print("mean is"+str(mean))

import pandas as pd
import plotly.express as px
df= pd.read_csv("class2.csv")

fig= px.scatter(df,x= "Student Number",y= "Marks")
fig.update_layout(shapes=[dict(type='line',y0= mean, y1= mean, x0= 0, x1= totalEnteries)])
fig.show()