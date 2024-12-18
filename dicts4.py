dict1 = {'a': 12, 'b': 25, 'c': 9}
dict2 = {'A': 100, 'b': 200, 'C': 300}

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)
