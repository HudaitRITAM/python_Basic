name = ("Ritam", "Ritwika", "Ritam")
comp = ("IBM", "Google", "IBM")
zipped1 = list(zip(name,comp))   # to get the output as list
zipped2 = set(zip(name,comp))
zipped3 = dict(zip(name,comp))
print(zipped1)
print(zipped2)
print(zipped3)