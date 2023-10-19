import requests
import json
import pickle
r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# print(r.json()) raise an error because response is not a json object. 

with open ("data-iris.txt","w") as f:
    f.write(r.text)

with open ("data-iris.txt","r") as f:
    x=f.read()
    data_list=(x.split("\n"))

newdata_list=[]
for i in data_list:
    i=[i]
    newdata_list.append(i)

pickle_data=pickle.dumps(newdata_list)

with open("Iris-data.pkl","wb") as f:
    f.write(pickle_data)
    
with open ("Iris-data.pkl","rb") as f:
    unpickle_data=pickle.loads(f.read())
print(unpickle_data)