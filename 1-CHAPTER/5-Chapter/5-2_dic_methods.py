a ={"name":"smita","from":"india","marks":[1,2,3]}
print(a.items()) # a.items() => returns a list of (key,value) tuples 

print(a.keys())
print(a.values())

b = {"graduate":'IMS'}
a.update(b)
print(a)

c = {"doctor":5,"engg.":"passion","bhuppi":{"megh":"girls"}}
a.update(c)
print(a)
