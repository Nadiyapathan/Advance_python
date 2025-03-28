import pandas as pd
#Dictionary wiith sample data
data={
    "name":["nadiya","bujji","ayishu"],
    "age":[25,20,35],
    "city":["new york","london","paris"]
}
#create a dataframe
df = pd.DataFrame(data)
#Display the Dataframe
print(df)