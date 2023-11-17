d= {
    'age':20,
    'height':1.73,
    'color':"Pink"
}
print(d["age"])
d['age'] = 21
print(d["age"])
print(d["height"])
d['height'] = 1.8
print(d["height"])
print(d["color"])
d['color'] = "Purple"
print(d["color"])
print(d.keys())
print(d.values())
print(d.items())
if 'age' in d:
    print(d['age'])