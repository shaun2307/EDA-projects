import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("transformed_data.csv")
# data2 = pd.read_csv("raw_data.csv")
print(data)


# The data we are using contains the data on covid-19 cases and their impact on GDP from December 31, 2019, to October 10, 2020.

# Data Preparation
# The dataset that we are using here contains two data files. One file contains raw data, and the other file contains transformed one. But we have to use both datasets for this task, as both of them contain equally important information in different columns. So let’s have a look at both the datasets one by one:

# print(data.head())
# After having initial impressions of both datasets, I found that we have to combine both datasets by creating a new dataset. But before we create a new dataset, let’s have a look at how many samples of each country are present in the dataset:

print(data["COUNTRY"].value_counts())

# So we don’t have an equal number of samples of each country in the dataset. Let’s have a look at the mode value:

data["COUNTRY"].value_counts().mode()

# So 294 is the mode value. We will need to use it for dividing the sum of all the samples related to the human development index, GDP per capita, and the population. Now let’s create a new dataset by combining the necessary columns from both the datasets:



code = data["CODE"].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data.loc[data["COUNTRY"] == i, "TC"]).sum())
    td.append((data.loc[data["COUNTRY"] == i, "TD"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data.loc[data["COUNTRY"] == i, "POP"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                               columns = ["Country Code", "Country", "HDI", 
                                          "Total Cases", "Total Deaths", 
                                          "Stringency Index", "Population"])
print(aggregated_data.head())