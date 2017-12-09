fam = {1:"kotireddy",2:"ramanna",3:"brahmareddy",4:"sandhya",5:"ashok"}
print(len(fam))

reddy=['name','age','class','gen','sal']
print(dict.fromkeys(reddy))

print(fam.get(2))

print(3 in fam)

print(list(fam.items()))

print(fam.keys())

print(fam.values())

fam.setdefault("D",15)
print(fam)