Marks={
    "haseeb" : 100,
    "hassan" : 80,
    "aqib" : 50
}
print(Marks.items())
print(Marks.keys())
print(Marks.values())
Marks.update({"haseeb":99})
print(Marks)

print(Marks.get("haseeb"))
marks=Marks.pop('key', 'default_value')