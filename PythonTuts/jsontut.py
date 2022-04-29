import json

datu ='{"var1":"Tanya","var2":"siopy"}'
# print(datu)
parsed = json.loads(datu)
# print(parsed['var1'])
# print(type(parsed))



data2 ={
    "pilla":['yellow','orange','pink'],
    "wire":['round','square','triangle'],
    "colth":('dirty',50,'bheek'),
    "tanya":True
}

# gh= json.dumps(data2)
# print(gh)
gh= json.dumps(data2,sort_keys=True)
print(gh)
