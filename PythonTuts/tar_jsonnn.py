import json

data = '{"Tarun" : "star" , "yoyo" : "lol"}'
pars = json.loads(data)
print(pars)
print(pars["yoyo"])

# load text file lata ha jis ma supporting json document hota ha us ko python object ma convert karta ha

data = {
    "name" : ["harry" , "tarun " ],
    "work" : ["engineer" , "engineer"],
    "money" : (0.001 , 990.4)

}
print(json.dumps(data))
