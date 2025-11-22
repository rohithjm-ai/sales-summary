import pandas as pd

df=pd.read_csv("input_file.csv")
df['total']=df['Quantity']*df['Price']
summary=df.groupby('Product')['total'].sum().reset_index()
summary=summary.sort_values(by="total",ascending=False)
print(summary)