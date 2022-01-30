#step 1
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
#step 2
df=pd.read_csv("medium.csv")
data = df["reading_time"].tolist()
#step3
population_mean = statistics.mean(data)
#step 4
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

#Step 5
ml=[]
for i in range(0,100):
    r=randomSetOfMean(30)
    ml.append(r)

#step 6
def plot_graph(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig=ff.create_distplot([df],["result"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1], mode="lines", name="mean"))
    fig.show()
#calling function
plot_graph(ml)

mean = statistics.mean(ml)
sd=statistics.stdev(ml)
print("mean=",mean)
print("Standard deviation=",sd)
#step 7
fsds,fsde=mean-sd,mean+sd
ssds,ssde=mean-(2*sd),mean+(2*sd)
tsds,tsde=mean-(3*sd),mean+(3*sd)

#step 8
ml1=[]
for i in range(0,1000):
    r=randomSetOfMean(60)
    ml1.append(r)

#step 9
plot_graph(ml1)

mean2 = statistics.mean(ml1)
z_score = (mean2-mean)/sd
print(z_score)