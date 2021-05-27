import csv
import plotly.express as px
import numpy as np
def getdatasource(datapath):
    sizeoftv=[]
    average= []
    with open(datapath) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
           sizeoftv.append(float[row["Size of T.V."]])
           average.append(float[row["Average time spent watching TV in a week (hours)"]])
    return {"x":sizeoftv ,"y":average}

def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation=",corelation[0,1])
def setup():
    datapath="data/data1.csv"
    datasource= getdatasource(datapath)
    findcorelation(datasource)
setup()