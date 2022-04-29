#Dictionary is defined as the key value pairs
d1 = { }
#print(type(d1))
d2 ={"Tanya": "Soup", "Panya": "Ramen", "Danya":"Kimchi", "Chikda":{"B":"potty","L":"Sotty","D":"Roti"}}
#print(d2["Chikda"]["L"])
#print(d2["Chikda"])
"""d2["Kiba"]={"Dhai Balle"}
d2[200]={"Nali"}
del d2[200]"""
#d3=d2 use copy function
#d3=d2.copy()
#del d3["Tanya"]
#print(d2)
print(d2.get("Tanya"))
#d2.update({"Roxxy": "Mochi"})
#print(d2.get("Roxxy"))
print(d2.keys())
print(d2.items())
print(d2.values())