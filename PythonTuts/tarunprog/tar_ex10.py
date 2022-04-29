import pickle
import requests

r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
data = r.text
with open("iris_ex10.txt", 'w') as f:
    f.write(data)
with open("iris_ex10.txt", 'r') as f1:
    content = f1.read().split("\n")
"""print(content) to see thing"""

file_obj = open("iris_picklle.pkl", 'wb')
pickle.dump(content, file_obj)
file_obj.close()

file_rd = open("iris_picklle.pkl", 'rb')
detail = pickle.load(file_rd)
print(detail)
