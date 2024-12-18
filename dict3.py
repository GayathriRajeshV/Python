a={'Era':12,'Shiv':67,'Dheer':53,'Arav':4}

for k,v in a.items():
    if v >=50:
        a.update({k:'Pass'})
    else:
        a.update({k:'Fail'})
print(dict(a))
        
