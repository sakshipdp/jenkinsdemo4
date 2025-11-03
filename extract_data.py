import requests
import pandas as pd 

requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()
df = pd.Dataframe(data)
df = df [["id","name"]]
print(df)
